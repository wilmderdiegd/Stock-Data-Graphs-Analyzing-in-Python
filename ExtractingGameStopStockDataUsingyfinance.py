# Import required library
import yfinance as yf

# Create a Ticker object for GameStop (GME)
gme = yf.Ticker("GME")

# Fetch GameStop's stock data for the maximum period available
gme_data = gme.history(period="max")

# Reset index to ensure 'Date' becomes a column
gme_data.reset_index(inplace=True)

# Display the first five rows of the dataset
gme_data.head()
