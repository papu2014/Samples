# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:10:40 2020

@author: Admin
"""
import numpy as np
from tensorflow import keras
model = keras.models.Sequential()
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(16, input_shape=(3, 2)))
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.Dense(4))
model.compile(loss='mean_squared_error', optimizer='SGD')

x = np.array([[[1, 2], [3, 4], [5, 6]]])

y = model.predict(x)

print(y.shape)
model.summary()
model.layers
hidden1=model.layers[1]
weights, biases = hidden1.get_weights()
weights
weights.shape  #(6, 16)
biases
biases.shape  #(16,)
