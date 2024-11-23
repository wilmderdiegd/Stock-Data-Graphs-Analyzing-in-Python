# Import required library
import yfinance as yf

# Create a Ticker object for Tesla
tesla = yf.Ticker("TSLA")

# Fetch Tesla's stock data for the maximum period available
tesla_data = tesla.history(period="max")

# Reset index to ensure 'Date' becomes a column
tesla_data.reset_index(inplace=True)

# Display the first five rows of the dataset
tesla_data.head()
