import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

# Define time frame
start = dt.datetime(2020, 3, 3)
end = dt.datetime.now()

# Load Data
ticker = 'AAPL'
data = yf.download(ticker, start=start, end=end)
print(data.columns)

data = data[['Open', 'High', 'Low', 'Close']]
data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)

# Visualization
ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.set_title('{} Share Price'.format(ticker), color='white')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data[['Date', 'Open', 'High', 'Low', 'Close']].values, width=0.5, colorup='#00ff00', colordown='#ff0000')
plt.show()
