import os
from pandas_datareader import data as pdr
import pandas as pd

import datetime
import yfinance as yf
import requests
import bs4 as bs
import pickle
from tkinter.ttk import Progressbar
from tkinter import * 

outdir = 'StockData'
yf.pdr_override()

def createStockPath():
    if not os.path.exists(outdir):
        os.mkdir(outdir)

def loadStock(ticker, start, end):
    createStockPath()
    data = pdr.get_data_yahoo(ticker,start=start, end=end)
    data.to_csv('{}/{}.csv'.format(outdir,ticker))

def getFortune500Ticker():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        ticker = ticker.rstrip("\n")
        tickers.append(ticker)
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)

def loadStockList(start, end, Progressbar, root):
    createStockPath()
    tickers = []
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
    x = 0
    for ticker in tickers:
        loadStock(ticker,start,end)
        x = x + 1
        Progressbar['value'] = x
        root.update_idletasks() 
