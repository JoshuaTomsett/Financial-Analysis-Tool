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

no_sims = 20
n = 100 # number of days
mu = 0.1

S0 = stockdata.current_price(ticker)
sigma = stockdata.stock_std(ticker, 100)
dt = 1/n

### Simulate

prices = np.empty((n+1, no_sims))
prices[0] = np.full(no_sims, S0)


for i in range(1, n+1): # for each step
    drift_shock = 1 + mu * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1, size=(no_sims, 1)).T
    prices[i] = np.multiply(prices[i-1], drift_shock)

days = np.arange(0, n+1)

plt.plot(days, prices)
plt.ylabel('Price')
plt.xlabel('Days')
plt.title(ticker)
plt.show()


### TO DO 

# move to a function, func(ticker, no_sims, n, sigma)

# sigma (standard deviation) - std of percentage change

# axis labels

# title

# bar chart