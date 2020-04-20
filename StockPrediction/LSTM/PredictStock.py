# Predict stock prices for a given date range
# Author: Oscar Kosar-Kosarewicz

import pandas as pd
from keras.models import load_model
import numpy as np
from StockPrediction.LSTM.CreateTrainingData import process_data, denormalize
from os import path



def predict_stocks(stock_data):
    """
    stock_data columns:
    Open,High,Low,Close,Adj Close,Volume

    :type stock_data: pandas.Dataframe
    """
    model_path = path.join(path.dirname(__file__), 'LSTM_model')
    metadata_path = path.join(path.dirname(__file__), 'LSTM_model_metadata.npy')
    model = load_model(model_path)
    model_metadata = np.load(metadata_path, allow_pickle=True).item()
    x, y, dates, min_price, max_price = process_data(stock_data, model_metadata['batch_size'],
                                                     model_metadata['time_steps_in_batch'])
    predictions = model.predict(x, batch_size=model_metadata['batch_size']).flatten()
    predictions = denormalize(predictions, min_price, max_price)

    results = pd.DataFrame({'Date': dates, 'Prediction': predictions})
    results['Date'] = results['Date'].str.decode('utf-8')
    return results


if __name__ == '__main__':
    stock_name = 'abc'
    data_source = f'../../StockData/{stock_name}.csv'
    data = pd.read_csv(data_source)
    print(predict_stocks(data))
