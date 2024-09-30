import pandas as pd
import numpy as np
import yfinance as y
import matplotlib.pyplot as plt
# panhandler lets you click and drag
# zoom_factory lets you zoom in with your scroll wheel
from mpl_interactions import panhandler, zoom_factory
from datetime import datetime, timedelta


# Gets the latest date 
latest_date = datetime.now().date() + timedelta(days=1)

# BRK.A fucks w the graph - seek help for this
symbols = ['LMT', 'AAPL', 'MS', 'QCOM', 'JPM','BRK-B','NVDA','TTWO']
start_time = '2006-09-13'
end_time = latest_date

# Fetches the symbols and the dates from yahoo finance 
stock_data = y.download(symbols, start=start_time, end=end_time)

# Adj Close is the adjusted closing price of the stock
adj_date = stock_data["Adj Close"]

# plots the figure on multiple axes 
figure,axis = plt.subplots(figsize=(14, 7))


# Plot each stock individually
for symbol in symbols:
    adj_date[symbol].plot(ax = axis,label=symbol )



plt.title("Stocks in Arush's Portfolio")
plt.xlabel("Date")
plt.ylabel("Value")

disconnect_zoom = zoom_factory(axis)
handler = panhandler(figure)

plt.legend()
plt.show()
