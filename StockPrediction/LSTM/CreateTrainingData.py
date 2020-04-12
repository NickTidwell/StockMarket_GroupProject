# Create training data for LST
# Author: Oscar Kosar-Kosarewicz

import numpy as np
from sklearn.model_selection import train_test_split

index_of_target_variable = 3  # close price


def create_timeseries(data, time_steps_in_batch):
    num_batches = data.shape[0] - time_steps_in_batch
    entries_per_sample = data.shape[1]
    x = np.zeros((num_batches, time_steps_in_batch, entries_per_sample))
    y = np.zeros((num_batches,))
    for i in range(num_batches):
        x[i] = data[i:i + time_steps_in_batch]
        y[i] = data[i + time_steps_in_batch, index_of_target_variable]
    return x, y


def generate_training_data(stock_name, time_steps_in_batch):
    data_source = f'../../StockData/{stock_name}.csv'

    data = np.genfromtxt(data_source, delimiter=',')
    data = np.delete(data, 0, axis=0)  # delete labels
    data = np.delete(data, 0, axis=1)  # delete dates

    # normalize each column
    data = data / data.max(axis=0)

    train_data, test_data = train_test_split(data, train_size=.8, test_size=.2, shuffle=False)

    x_train, y_train = create_timeseries(train_data, time_steps_in_batch)
    x_test, y_test = create_timeseries(test_data, time_steps_in_batch)
    return x_train, y_train, x_test, y_test


if __name__ == '__main__':
    x_train, y_train, x_test, y_test = generate_training_data('AAL', 10)
    np.save('TrainingX', x_train)
    np.save('TrainingY', y_train)
    np.save('TestingX', x_test)
    np.save('TestingY', y_test)
