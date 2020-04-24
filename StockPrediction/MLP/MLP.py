from  StockPrediction.MLP.split_data import DataSplitter
from StockPrediction.MLP import plot_MLP
import keras
import numpy as np
from keras.utils.vis_utils import plot_model
from sklearn.preprocessing import normalize
import os

def importMLPStock(stock):
    
    data_file_path =  f"../../StockData/{stock}.csv"
    datasource = DataSplitter(data_file_path, 0.9)
    length = datasource.length // 100
    datasource.create_training(length)
    datasource.create_testing(length)


    trainX = datasource.trainX  
    trainY = datasource.trainY

    testX = datasource.testX
    testY = datasource.testY

    model = keras.models.Sequential()
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(1, activation='relu'))

    keras.optimizers.Adam(learning_rate=0.1)
    model.compile(loss="mean_squared_error", optimizer="adam")  # adam is the chosen optimizer

    model.fit(trainX, trainY, epochs=100, batch_size = 100, validation_data=(testX, testY))

    model.save('MLP_model.h5')

if __name__ == '__main__':
    importMLPStock('amzn')