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
global progress
def createStockPath():
    if not os.path.exists(outdir):
        os.mkdir(outdir)

def loadStock(ticker, start, end):
    if (end - start).days < 365:
        print("Must have greater then 365 days to import")
        return False
    createStockPath()
    data = pdr.get_data_yahoo(ticker,start=start, end=end)
    if(len(data) == 0):
        return False
    data.to_csv('{}/{}.csv'.format(outdir,ticker))
    return True
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


def loadStockList(start, end, progressbar, root, label):
    tickers = []
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
    x = 0
    label["text"] = "running..."
    for ticker in tickers:
        loadStock(ticker,start,end)
        x=x+1
        progressbar.after(0, progress(x,progressbar))
        progressbar.update() # Force an update of the GUI
    label["text"] = "Done."

def progress(val, bar):
    bar['value'] = val