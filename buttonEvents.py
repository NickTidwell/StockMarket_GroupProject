from importModule import loadStock
from tkinter import *
import importForm
import csv
import csvTable
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

def displayGrid(txt):
    dow = Tk()
    app = csvTable.CreateTable(txt, dow)
    app.mainloop()

def loadStockClicked(txt):
    displayGrid(txt.get())

def importStockClicked():
    importForm.ImportFrame()

def importSingleStock(txt,start,end):
    loadStock(txt.get(),start.get_date(),end.get_date())

def plotStock(txt):
    #Modfied from code in Playground PlotStock.py
    stock_name = txt.get()
    y_value = 'Open'
    data_file_path = f'StockData/{stock_name}.csv'
    data = pd.read_csv(data_file_path)
    title = f'{stock_name.upper()} Stock'
    plt.figure(figsize=(12, 6), num=title)
    ax = plt.subplot(1, 1, 1)
    plt.title(title)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
    ax.xaxis.set_minor_locator(ticker.MaxNLocator(100))
    plt.xlabel('Date')
    plt.ylabel(f'{y_value} Price ($)')
    ax.plot(data['Date'], data[y_value])
    plt.show()

    

