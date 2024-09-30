import pandas as pd
import numpy as np
import yfinance as y
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta

# Gets the latest date 
latest_date = datetime.now().date() + timedelta(days=1) 

# For stocks like Berkshire, with a ".", u have to use a "-"
symbols = ['LMT','AAPL','MS','QCOM','JPM','BRK-A']
start_time = '2006-09-13'
end_time = latest_date

# Fetches the symbols and the dates from yahoo finance 
stock_data = y.download(symbols,start = start_time, end = end_time)

# Adj Close is the adjusted closing price of the stock
print(stock_data['Adj Close'])
