### CONTAINS ALL TOOL FUNCTIONS

import stockdata
import numpy as np

def calcRegressionLine(x, y):
    """
    Calculates the regression line using the least squares method.

    Args:
        x: Array of x values
        y: Array of y values

    Returns:
        a,b
        The slope (a) and intercept (b) of the regression line (y = ax+ b)
    """

    n = len(x)
    Sx = sum(x)
    Sx2 = sum(i*i for i in x)
    Sy = sum(y)
    Sxy = sum(a * b for a, b in zip(x, y))

    a = (n*Sxy - Sx*Sy) / (n*Sx2 - Sx**2)
    b = (Sx2*Sy - Sx*Sxy) / (n*Sx2 - Sx**2)

    return a,b


def GBM(ticker, no_sims, n):
    """Calculates and returns a numpy array that contains the GBM (Geometric Brownian Motion) simulation

    Args:
        ticker (string): The stock ticker
        no_sims (int): The number of simulations to be performed
        n (int): The number of days

    Returns:
        prices: numpy array of simulated prices
    """

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


