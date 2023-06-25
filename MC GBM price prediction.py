### Program that uses GBM (Geometric Brownian Motion) to predict stock prices

### GBM formula: St = S * (mu * dt + sigma * r * sqrt(dt))

### St = price at time = t
### S = start price
### mu = expected return
### dt = change in time
### sigma = standard deviation of returns
### r = random value


import stockdata
import numpy as np

ticker = 'TSLA'

yearData = stockdata.get_data_days(ticker, 365)
price_array = np.array(yearData) # numpy array of close price data
