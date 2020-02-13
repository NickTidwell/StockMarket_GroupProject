import os
from pandas_datareader import data as pdr
import pandas as pd

import datetime
import yfinance as yf


outdir = 'StockData'
yf.pdr_override()

def createStockPath():
    if not os.path.exists(outdir):
        os.mkdir(outdir)

def loadStock(ticker, start, end):
    data = pdr.get_data_yahoo(ticker,start=start, end=end)
    data.to_csv('{}/{}.csv'.format(outdir,ticker))