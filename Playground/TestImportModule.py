import numpy as numpy
import yfinance as yf
import datetime
from pandas_datareader import data as pdr
import pandas as pd
import requests
import bs4 as bs
import pickle
import os

yf.pdr_override()
outdir = 'StockData'

#Gets List of Fortune 500 Tickers
getSymbols = True #Refreshes symbol only if True, extract this to function in dev
loadStockData = True #This takes a long time wouldnt recommend calling after first use

resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})
tickers = []

if(getSymbols):
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        ticker = ticker.rstrip("\n")
        tickers.append(ticker)
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
else:
    with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

#Gets Stock Data for today on tickers and stores to CSV
start = datetime.datetime(2020,1,1)
end   = datetime.datetime.today()

if not os.path.exists(outdir):
    os.mkdir(outdir)

if(loadStockData):
    for ticker in tickers:
        data = pdr.get_data_yahoo(ticker,start=start, end=end)
        data.to_csv('{}/{}.csv'.format(outdir,ticker))

