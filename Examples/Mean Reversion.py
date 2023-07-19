import sys
sys.path.append('..')
from analysisTools import calculate_moving_average
import stockdata
import numpy as np
import matplotlib.pyplot as plt


ticker = 'TSLA'
data = stockdata.get_data_days(ticker, 600)
close_prices = []
for i in data:
    close_prices.append(i)


window_size = 20
moving_averages = calculate_moving_average(close_prices, window_size)


plt.figure(figsize=(10, 6))
plt.plot(close_prices, label='Closing Prices')
plt.plot(range(window_size - 1, len(close_prices)), moving_averages, label='Moving Average')
plt.xlabel('Period')
plt.ylabel('Price')
plt.title('Closing Prices and Moving Averages')
plt.legend()
plt.grid(True)
plt.show()