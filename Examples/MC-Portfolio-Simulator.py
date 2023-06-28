### Program that uses the GBM program to simulate an entire portfolio

import sys
sys.path.append('..')
import stockdata
from analysisTools import GBM_portfolio
import numpy as np
import matplotlib.pyplot as plt


portfolio = ["TSLA", "^FTSE", "AMZN"]
no_sims = 100
n = 100 # number of days

value = GBM_portfolio(portfolio, no_sims, n)
days = np.arange(0, n+1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(days, value)
ax1.set_ylabel('Portfolio Value')
ax1.set_xlabel('Days')
ax1.set_title("Stock Portfolio Value Simulation")

# Plot the distribution of final prices
ax2.hist(value[-1], bins=20)
ax2.set_ylabel('Frequency')
ax2.set_xlabel('Portfolio Value')
ax2.set_title(f"Value Histogram - $\mu = {np.mean(value[-1])}$")

plt.show()