import buttonEvents as be
from StockPrediction.LSTM.PredictStock import predict_stocks
import csv
import  datetime
import pandas as pd
import os


def createReportPath(path):
    if not os.path.exists(path):
        os.mkdir(path)

def buildReport():
    createReportPath('reports')
    csv_columns = ['ticker', 'percent_change']
    csv_file =   'report' + str(datetime.date.today()) + '.csv'
    file_Path = f'Reports/{csv_file}'

    with open(file_Path,'w') as csvFile:
        writer = csv.DictWriter(csvFile,fieldnames=csv_columns)
        writer.writeheader()
        stockList = be.updateStockList()
        for stock in stockList:
            data = {'ticker': stock, 'percent_change': predictPercentChange(stock)}
            writer.writerow(data)

def predictPercentChange(stock_name):
    data_source = f'StockData/{stock_name}.csv'
    data = pd.read_csv(data_source)
    prediction_data = predict_stocks(data)
    next_value = prediction_data['Prediction'].values[-1]
    prev_pred = prediction_data['Prediction'].values[-2]
    return (next_value-prev_pred)/ prev_pred * 100