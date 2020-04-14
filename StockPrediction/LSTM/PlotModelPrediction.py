# Plots model's stock predictions
# Author: Oscar Kosar-Kosarewicz

import matplotlib.pyplot as plt
import pandas as pd
from keras.models import load_model
import numpy as np

def trim_data(x, y, batch_size):
    rows_to_drop = x.shape[0] % batch_size
    if rows_to_drop > 0:
        x = x[:-rows_to_drop]
        y = y[:-rows_to_drop]
        return x, y
    return x, y

def plot_prediction(model_path):
    model = load_model(model_path)
    x = np.load('TestingX.npy')
    y = np.load('TestingY.npy')
    dates = np.load('TestingDates.npy')
    dates_shifted = dates[:-1]
    x = x[1:]
    dates_shifted, x = trim_data(dates_shifted, x, 10)

    title = f'Stock Prediction'
    plt.figure(num=title)
    ax = plt.subplot(1, 1, 1)
    plt.title(title)
    #ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
    #ax.xaxis.set_minor_locator(ticker.MaxNLocator(100))
    plt.xlabel('Date')
    plt.ylabel(f'Price')
    actual_line, = ax.plot(dates, y)
    predicted_line, = ax.plot(dates_shifted, model.predict(x, batch_size = 10))
    actual_line.set_label('Actual')
    predicted_line.set_label('Predicted')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    plot_prediction('LSTM_model')
