from split_data import DataSplitter
import tensorflow as tf
import plot_MLP
import keras
import numpy as np
from keras.utils.vis_utils import plot_model
from sklearn.preprocessing import normalize


datasource = DataSplitter("../../StockData/amzn.csv", 0.9)
datasource.create_training(10)
datasource.create_testing(10)

trainX = datasource.trainX/10000  # *********change normalization method
trainY = datasource.trainY/10000  # *** same method here... used to make sure the weights dont grow to large
# trainX = trainX / np.linalg.norm(trainX)
# trainY =  trainY / np.linalg.norm(trainY)

testX = datasource.testX/10000
testY = datasource.testY/10000
# testX =  testX / np.linalg.norm(testX)
# testY =  testY / np.linalg.norm(testY)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(1, activation=tf.nn.relu))

model.compile(loss="mean_squared_error", optimizer="RMSProp")  # adam is the chosen optimizer
model.fit(trainX, trainY, epochs=100)
model.save('MLP_model')

plot_MLP.plotter('MLP_model')

print(model.evaluate(testX, testY))
