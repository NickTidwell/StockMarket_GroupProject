from importModule import loadStock
from tkinter import *
import importForm
import reportViewForm
import csv
import csvTable
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from StockPrediction.LSTM.PredictStock import predict_stocks
from os import listdir, path
from StockPrediction.MLP.MLP import importMLPStock     # used for MLP prediction
from reportModule import buildReport
def displayGrid(txt):
    dow = Tk()
    app = csvTable.CreateStockTable(txt, dow)
    app.mainloop()

def loadStockClicked(txt):
    displayGrid(txt.get())

def importStockClicked():
    importForm.ImportFrame()
    updateStockList()

def viewReportClicked():
    reportViewForm.ReportFrame()

def importSingleStock(txt,start,end,status):
    success = loadStock(txt.get(),start.get_date(),end.get_date())
    if(success == True):
        status["text"] = "Success"
        updateStockList()
    else:
        status["text"] = "Failed"

def buildReportM():
    buildReport()
def plotStock(txt):
    #Modfied from code in Playground PlotStock.py
    stock_name = txt.get()
    y_value = 'Open'
    data_file_path = path.join(path.dirname(__file__), f'StockData/{stock_name}.csv')
    data = pd.read_csv(data_file_path)
    title = f'{stock_name.upper()} Stock'
    plt.figure(figsize=(10, 5), num=title)
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
    if path.exists(f'stockData'):
        for file in listdir(f'StockData'):
            file = file.replace('.csv', '')
            stockList.add(file)
        return tuple(stockList)
    return tuple()


def reportList():
    report = set()
    if path.exists(f'reports'):
        for file in listdir(f'reports'):
            report.add(file)
        return tuple(report)
    return tuple()

    changeVal =  (next_value - prev_pred)/prev_pred * 100
    print("Stock: {} , {}".format(stock_name,changeVal))
    return changeVal
def graphPrediction(txt):
    # Author Oscar-Kosarewicz
    # Modified by Nick T
    # import predictor data into Dataframe
    stock_name = txt.get()
    data_source = path.join(path.dirname(__file__), f'StockData/{stock_name}.csv')
    data = pd.read_csv(data_source)
    
    datesMLP, predictionsMLP = importMLPStock(stock_name)  # call MLP method


    # Calculate predictions
    prediction_data = predict_stocks(data)
    predicted_value = prediction_data['Prediction'].values[-1]
   # print(prediction_data["Prediction"][-1])
    # Set up plot
    title=f'{stock_name.upper()} Price Prediction'
    plt.figure(figsize=(10, 5), num=title)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MaxNLocator(5))   # number of major ticks
    ax.xaxis.set_minor_locator(ticker.MaxNLocator(25))  # number of minor ticks

    # Plot actual stock price
    actual_line, = ax.plot(data['Date'], data['Close'])
    actual_line.set_label('Actual')

    # Plot LSTM predicted stock price
    predicted_lineLSTM, = ax.plot(prediction_data['Date'], prediction_data['Prediction'])
    predicted_lineLSTM.set_label('Predicted LSTM')

    # Plot MLP predicted stock price
    predicted_lineMLP, = ax.plot(datesMLP, predictionsMLP)
    predicted_lineMLP.set_label('Predicted MLP')

    # Show Plot
    ax.legend()
    plt.show()


