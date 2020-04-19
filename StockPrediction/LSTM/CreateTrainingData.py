# Create training data for LST
# Author: Oscar Kosar-Kosarewicz

import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

index_of_target_variable = 4  # close price


def create_timeseries(data, time_steps_in_batch):
    num_batches = data.shape[0] - time_steps_in_batch
    entries_per_sample = data.shape[1]-1
    x = np.zeros((num_batches, time_steps_in_batch, entries_per_sample))
    y = np.zeros((num_batches,))
    dates = np.zeros((num_batches,), dtype=np.dtype('a16'))
    for i in range(num_batches):
        x[i] = data.iloc[i:i + time_steps_in_batch, 1:]
        y[i] = data.iloc[i + time_steps_in_batch, index_of_target_variable]
        dates[i] = data.iloc[i + time_steps_in_batch, 0]
    return x, y, dates


def generate_training_data(stock_name, time_steps_in_batch):
    data_source = f'../../StockData/{stock_name}.csv'


    data = pd.read_csv(data_source)
    # normalize each column
    data2 = data.iloc[:, 1:]
    data.iloc[:, 1:] = (data2-data2.min())/(data2.max()-data2.min())

    train_data, test_data = train_test_split(data, train_size=.8, test_size=.2, shuffle=False)

    x_train, y_train, __ = create_timeseries(train_data, time_steps_in_batch)
    x_test, y_test, dates = create_timeseries(test_data, time_steps_in_batch)
    np.save('TestingX', x_test)
    np.save('TestingY', y_test)
    np.save('TestingDates', dates)
    return x_train, y_train, x_test, y_test


if __name__ == '__main__':
    x_train, y_train, x_test, y_test = generate_training_data('AAL', 10)
    np.save('TrainingX', x_train)
    np.save('TrainingY', y_train)