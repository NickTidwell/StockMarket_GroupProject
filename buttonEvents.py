from importModule import loadStock
from tkinter import *
import importForm
import csv
import csvTable
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from StockPrediction.LSTM.PredictStock import predict_stocks
from os import listdir
def displayGrid(txt):
    dow = Tk()
    app = csvTable.CreateTable(txt, dow)
    app.mainloop()

def loadStockClicked(txt):
    displayGrid(txt.get())

def importStockClicked():
    importForm.ImportFrame()
    updateStockList()

def importSingleStock(txt,start,end,status):
    success = loadStock(txt.get(),start.get_date(),end.get_date())
    if(success == True):
        status.set("Success")
        updateStockList()
    else:
        status.set("Failed")

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

def updateStockList():
    stockList = set()
    for file in listdir(f'StockData'):
        file = file.replace('.csv', '')
        stockList.add(file)
    return tuple(stockList)
def graphPrediction(txt):
    # Author Oscar-Kosarewicz
    # Modified by Nick T
    # import predictor data into Dataframe
    stock_name = txt.get()
    data_source = f'StockData/{stock_name}.csv'
    data = pd.read_csv(data_source)

    # Calculate predictions
    prediction_data = predict_stocks(data)

    # Set up plot
    plt.title(f'{stock_name.upper()} Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Price')
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MaxNLocator(5))   # number of major ticks
    ax.xaxis.set_minor_locator(ticker.MaxNLocator(25))  # number of minor ticks

    # Plot actual stock price
    actual_line, = ax.plot(data['Date'], data['Close'])
    actual_line.set_label('Actual')

    # Plot predicted stock price
    predicted_line, = ax.plot(prediction_data['Date'], prediction_data['Prediction'])
    predicted_line.set_label('Predicted')

    # Show Plot
    ax.legend()
    plt.show()


