# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tensorflow as tf
from tensorflow import keras
fashion_mnist = keras.datasets.fashion_mnist

(X_train_full,y_train_full) , (X_test,y_test) =fashion_mnist.load_data()

x_valid,  x_train = X_train_full[:50000]/255.0,  X_train_full[50000:]/255.0

y_valid,  y_train = y_train_full[:50000],  y_train_full[50000:]

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

