# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website with Tesla's revenue data
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Send a GET request to fetch the webpage content
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the revenue table
revenue_table = soup.find("table", attrs={"class": "historical_data_table table"})  # First matching table

# Extract rows from the table body
rows = revenue_table.find("tbody").find_all("tr")  # Get all rows from the table body
data = []

# Loop through each row to extract year and revenue data
for row in rows:
    year = row.find_all("td")[0].text.strip()  # Extract the year
    revenue = row.find_all("td")[1].text.strip()  # Extract the revenue
    data.append([year, revenue])  # Append as a list of year and revenue

# Create a DataFrame from the extracted data
tesla_revenue = pd.DataFrame(data, columns=["Year", "Revenue"])

# Clean the revenue column
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",", "").str.replace("$", "")  # Remove $, commas
tesla_revenue["Revenue"] = pd.to_numeric(tesla_revenue["Revenue"], errors="coerce")  # Convert to numeric

# Drop rows with missing revenue values (if any)
tesla_revenue.dropna(inplace=True)

# Display the last five rows of the DataFrame
print(tesla_revenue.tail())