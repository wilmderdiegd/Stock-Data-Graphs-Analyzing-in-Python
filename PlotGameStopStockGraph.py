# Import required libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch GameStop stock data using yfinance
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")

# Step 2: Reset the index to make 'Date' a column
gme_data.reset_index(inplace=True)

# Step 3: Ensure 'Date' column is in datetime format
gme_data['Date'] = pd.to_datetime(gme_data['Date'])

# Step 4: Define the graph plotting function (reuse from Question 5)
def make_graph(data, title):
    """
    Plots the stock's closing price over time.

    Parameters:
    - data: DataFrame containing stock data with a 'Date' and 'Close' column.
    - title: Title for the graph.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Close'], label='Close Price', linewidth=2)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Close Price (USD)', fontsize=12)
    plt.title(title, fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.show()

# Step 5: Plot the GameStop stock graph
make_graph(gme_data, "GameStop Stock Data: Closing Price Over Time")
