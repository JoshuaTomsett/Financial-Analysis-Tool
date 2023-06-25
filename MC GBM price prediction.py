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
import matplotlib.pyplot as plt

ticker = 'TSLA'

price_array = np.array(stockdata.get_data_days(ticker, 100)) # numpy array of close price data

no_sims = 10
n = 100 # number of days
mu = 0.1

S0 = price_array[-1]
# sigma = np.std(price_array)
sigma = 0.3
dt = 1/n

### Simulate

prices = np.empty((101, 10))
prices[0] = np.full(10, S0)


for i in range(1, n+1): # for each step
    drift_shock = 1 + mu * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1, size=(no_sims, 1)).T
    prices[i] = np.multiply(prices[i-1], drift_shock)

time = np.arange(0, 101)
days = np.full(shape=(no_sims, n+1), fill_value=time).T

plt.plot(days, prices)
plt.show()


### TO DO 

# move to a function, func(ticker, no_sims, n, sigma)

# sigma (standard deviation)

# axis labels

# title

# bar chart