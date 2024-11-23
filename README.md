Stock Data Analysis and Visualization Assignment
Overview

This repository contains Python scripts and their respective outputs that demonstrate the use of yfinance and web scraping for extracting and analyzing stock data. It also includes visualizations for Tesla and GameStop stock performance, as well as their revenue trends.

The purpose of this repository is to fulfill the requirements of an assignment that involves extracting, processing, and visualizing stock and revenue data for Tesla (TSLA) and GameStop (GME).
Contents
1. ExtractingGameStopRevenueDataUsingWebScraping.py

    Description:
        This script uses web scraping to extract GameStop’s annual revenue data from the MacroTrends website.
        The revenue data is cleaned and stored in a pandas DataFrame, and the last five rows of the data are displayed.
    Output: Includes a screenshot showing the extracted revenue data for GameStop.

2. ExtractingGameStopStockDataUsingyfinance.py

    Description:
        This script uses the yfinance library to extract GameStop’s historical stock data.
        The data includes columns like Date, Open, Close, High, and Low.
        The script displays the first five rows of the extracted stock data.
    Output: Includes a screenshot of the first five rows of GameStop’s stock data.

3. UseWebscrapingtoExtractTeslaRevenueData.py

    Description:
        This script uses web scraping to extract Tesla’s annual revenue data from the MacroTrends website.
        The revenue data is cleaned and stored in a pandas DataFrame, and the last five rows of the data are displayed.
    Output: Includes a screenshot showing the extracted revenue data for Tesla.

4. StockDataGraphsAnalyzinginPython.py

    Description:
        This script consolidates the process of plotting stock data for both Tesla and GameStop.
        It uses a reusable make_graph function to visualize the stock's closing price trends over time.
    Output: Includes screenshots of line graphs for Tesla and GameStop stock data.

5. PlotTeslaStockGraph.py

    Description:
        This script visualizes Tesla’s stock data.
        It uses a custom make_graph function to plot Tesla’s closing price over time.
    Output: Includes a screenshot of the graph showing Tesla's historical stock performance.

6. PlotGameStopStockGraph.py

    Description:
        This script visualizes GameStop’s stock data.
        It uses a custom make_graph function to plot GameStop’s closing price over time.
    Output: Includes a screenshot of the graph showing GameStop's historical stock performance.
