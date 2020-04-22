import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import keras as ks
import numpy as np

def plotter(file_path):
    imported_model = tf.saved_model.load(file_path)

    testX = np.load("testX.npy")
    testY = np.load("testY.npy")
    Dates = np.load("Dates.npy")

    restored_model = tf.keras.models.load_model(file_path)
    prediction = restored_model.predict(testX)
    date = np.arange(len(prediction))
    
    ax1 = plt.subplot(1, 1, 1)
    line = ax1.plot(date, testY)
    line2 = ax1.plot(date, prediction)
    
    plt.show()
