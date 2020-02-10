import os
from pandas_datareader import data as pdr
import pandas as pd

import datetime
import yfinance as yf


outdir = 'StockData'
yf.pdr_override()

start = datetime.datetime(2020,1,1)
end   = datetime.datetime.today()

def createStockPath():
    if not os.path.exists(outdir):
        os.mkdir(outdir)

def loadStock(ticker):
    data = pdr.get_data_yahoo(ticker,start=start, end=end)
    data.to_csv('{}/{}.csv'.format(outdir,ticker))