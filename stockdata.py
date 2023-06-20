### Simple program to get historical stock data, for use in other programs

from pandas_datareader import data
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime , timedelta

yf.pdr_override()


def get_data(ticker,START_DATE,END_DATE, col):

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


END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
WEEK_DATE = datetime.now() - timedelta(days=30)
WEEK_DATE = WEEK_DATE.strftime('%Y-%m-%d')

ticker = 'TSLA'

week_price = get_data(ticker, WEEK_DATE, END_DATE, 'Adj Close')
weekGraph = create_plot(week_price)