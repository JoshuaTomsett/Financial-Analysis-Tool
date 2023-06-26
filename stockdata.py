### Simple program to get historical stock data, for use in other programs

from pandas_datareader import data
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime , timedelta

yf.pdr_override()


def get_data(ticker,START_DATE,END_DATE, col):

    stock_data = data.get_data_yahoo(ticker,start=WEEK_DATE,end=END_DATE)
    clean_data = stock_data[col]
    return clean_data.fillna(method='ffill') # returns only the data about prices


def get_data_days(ticker, days, col='Adj Close'):
    END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
    WEEK_DATE = datetime.now() - timedelta(days=days)
    WEEK_DATE = WEEK_DATE.strftime('%Y-%m-%d')
    stock_data = data.get_data_yahoo(ticker,start=WEEK_DATE,end=END_DATE)
    clean_data = stock_data[col]
    return clean_data.fillna(method='ffill') # returns only the data about prices


def create_plot(stock_data):
    plt.subplots(figsize=(12,8))
    plt.plot(stock_data)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=20)
    plt.show()


def current_price(ticker):
    week_price = get_data_days(ticker, 7)
    return week_price[-1]


def stock_std_mu(ticker, days):
    price_array = get_data_days(ticker, days)
    sigma = np.std(price_array.pct_change())

    daily_returns = price_array[1:] - price_array[:-1]
    mu = np.mean(daily_returns)

    return sigma, mu


if __name__ == '__main__':

    END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
    WEEK_DATE = datetime.now() - timedelta(days=30)
    WEEK_DATE = WEEK_DATE.strftime('%Y-%m-%d')
    ticker = 'TSLA'

    week_price = get_data_days(ticker, 30)
    print(week_price)
    weekGraph = create_plot(week_price)