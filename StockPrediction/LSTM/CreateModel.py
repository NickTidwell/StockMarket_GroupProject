# Create LST prediction model
# Author: Oscar Kosar-Kosarewicz

import numpy as np
import keras as ks
from StockPrediction.LSTM.CreateTrainingData import generate_training_data
from StockPrediction.LSTM.PlotLoss import plot_loss
from StockPrediction.LSTM.PlotModelPrediction import plot_prediction



def trim_data(x, y, batch_size):
    rows_to_drop = x.shape[0] % batch_size
    if rows_to_drop > 0:
        x = x[:-rows_to_drop]
        y = y[:-rows_to_drop]
        return x, y
    return x, y


def gen_data(stock_name):
    x_train, y_train, x_temp, y_temp = generate_training_data(stock_name, time_steps_in_batch)
    x_train, y_train = trim_data(x_train, y_train, batch_size)
    x_validate, x_test = np.array_split(x_temp, 2)
    y_validate, y_test = np.array_split(y_temp, 2)

    x_validate, y_validate = trim_data(x_validate, y_validate, batch_size)
    x_test, y_test = trim_data(x_test, y_test, batch_size)
    return x_train, y_train, x_validate, y_validate


def create_model(batch_size, time_steps_in_batch, hidden_layers_LSTM, hidden_layers_out, dropout):
    model = ks.Sequential()
    model.add(ks.layers.LSTM(hidden_layers_LSTM, batch_input_shape=(batch_size, time_steps_in_batch, x_train.shape[2]),
                             dropout=0,
                             recurrent_dropout=0, stateful=True,
                             kernel_initializer=ks.initializers.random_uniform(seed=0)))

    model.add(ks.layers.Dropout(dropout))
    model.add(ks.layers.Dense(hidden_layers_out, activation='relu'))
    model.add(ks.layers.Dense(1, activation='linear'))
    # optimizer = ks.optimizers.RMSprop(lr=.01)
    model.compile(loss='mean_squared_error', optimizer='adam')

    return model


if __name__ == '__main__':
    stock_name = 'amzn'
    batch_size = 10
    time_steps_in_batch = 20
    hidden_layers_LSTM = 100
    hidden_layers_out = 20
    dropout = 0

    x_train, y_train, x_validate, y_validate = gen_data(stock_name)

    model = create_model(batch_size, time_steps_in_batch, hidden_layers_LSTM, hidden_layers_out, dropout)
    csv_logger = ks.callbacks.CSVLogger('loss.csv', append=False)
    model.fit(x_train, y_train, epochs=200, batch_size=batch_size, verbose=2, shuffle=False,
              validation_data=(x_validate, y_validate), callbacks=[csv_logger])
    model.save('LSTM_model')
    plot_loss('loss.csv')
    plot_prediction('LSTM_model')
