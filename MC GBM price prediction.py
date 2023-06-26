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

def GBM(ticker, no_sims, n):
    # variables
    S0 = stockdata.current_price(ticker)
    sigma, mu = stockdata.stock_std_mu(ticker, 100)
    dt = 1/n
    
    # Simulate
    prices = np.empty((n+1, no_sims))
    prices[0] = np.full(no_sims, S0)

    for i in range(1, n+1): # for each step
        drift_shock = 1 + mu * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1, size=(no_sims, 1)).T
        prices[i] = np.multiply(prices[i-1], drift_shock)

    days = np.arange(0, n+1)

    return days, prices

ticker = "TSLA"
no_sims = 100
n = 100 # number of days

days, prices = GBM(ticker, no_sims, n) 
plt.plot(days, prices)
plt.ylabel('Price')
plt.xlabel('Days')
plt.title(f"Monte Carlo GBM - {ticker}\n" + "$S_t = S_0 * (\mu dt + \sigma \epsilon \sqrt{dt})$")
plt.show()



### TO DO 

# mu value

# bar chart