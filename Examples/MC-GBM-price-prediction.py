### Program that uses GBM (Geometric Brownian Motion) to predict stock prices

### GBM formula: St = S * (mu * dt + sigma * r * sqrt(dt))

### St = price at time = t
### S = start price
### mu = expected return
### dt = change in time
### sigma = standard deviation of returns
### r = random value

import sys
sys.path.append('..')
import stockdata
from analysisTools import GBM
import numpy as np
import matplotlib.pyplot as plt

ticker = "TSLA"
no_sims = 100
n = 100 # number of days

days, prices = GBM(ticker, no_sims, n)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.plot(days, prices)
ax1.set_ylabel('Price')
ax1.set_xlabel('Days')
ax1.set_title(f"Monte Carlo GBM - {ticker}\n" + "$S_t = S_0 * (\mu dt + \sigma \epsilon \sqrt{dt})$")

# Plot the distribution of final prices
ax2.hist(prices[-1], bins=20)
ax2.set_ylabel('Frequency')
ax2.set_xlabel('Price')
ax2.set_title(f"End Price Histogram - $\mu = {np.mean(prices[-1])}$")

plt.show()