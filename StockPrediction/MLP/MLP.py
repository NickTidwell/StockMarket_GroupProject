from  StockPrediction.MLP.split_data import DataSplitter
import tensorflow as tf
from StockPrediction.MLP import plot_MLP
import keras
import numpy as np
from keras.utils.vis_utils import plot_model
from sklearn.preprocessing import normalize
import os

def importMLPStock(stock):
    
    print("d is: ", os.getcwd())
    
    stock += ".csv"
    datasource = DataSplitter(f"StockData/amzn.csv", 0.9)
    length = datasource.length // 100
    print("length", length)
    datasource.create_training(length)
    datasource.create_testing(length)


    trainX = datasource.trainX  
    trainY = datasource.trainY  

    testX = datasource.testX
    testY = datasource.testY

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(1, activation=tf.nn.relu))

    tf.random.set_seed(13)
    keras.optimizers.Adam(learning_rate=0.1)
    model.compile(loss="mean_squared_error", optimizer="adam")  # adam is the chosen optimizer

    model.fit(trainX, trainY, epochs=100, batch_size = 100, validation_data=(testX, testY))

    model.save('MLP_model')

    plot_MLP.plotter('MLP_model')
