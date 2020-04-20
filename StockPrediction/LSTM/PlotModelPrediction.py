# Plots model's stock predictions
# Author: Oscar Kosar-Kosarewicz

import matplotlib.pyplot as plt
from keras.models import load_model
import numpy as np
from StockPrediction.LSTM.CreateTrainingData import  trim_data

def plot_prediction(model_path, batch_size):
    model = load_model(model_path)
    x = np.load('TestingX.npy')
    y = np.load('TestingY.npy')
    dates = np.load('TestingDates.npy')
    dates_shifted = dates[:]
    #x = x[1:]
    x = trim_data(x, batch_size)
    dates_shifted = trim_data(dates_shifted, batch_size)

    title = f'Stock Prediction'
    plt.figure(num=title)
    ax = plt.subplot(1, 1, 1)
    plt.title(title)
    #ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
    #ax.xaxis.set_minor_locator(ticker.MaxNLocator(100))
    plt.xlabel('Date')
    plt.ylabel(f'Price')
    actual_line, = ax.plot(dates, y)
    predicted_line, = ax.plot(dates_shifted, model.predict(x, batch_size = batch_size))
    actual_line.set_label('Actual')
    predicted_line.set_label('Predicted')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    plot_prediction('LSTM_model', 5)
