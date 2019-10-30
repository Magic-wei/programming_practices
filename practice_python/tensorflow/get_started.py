# from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras import layers

import numpy as np
import os

print("tf.keras version:", tf.keras.__version__)

# 1. Basic

# train from NumPy data
data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))

# model configuration
model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(32,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')])
# Configure a model for mean-squared error regression.
model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
              loss='mse',  # mean squared error
              metrics=['mae'])  # mean absolute error

# training
model.fit(data, labels, epochs=10, batch_size=32)

# you can also use validation data
val_data = np.random.random((100, 32))
val_labels = np.random.random((100, 10))
model.fit(data, labels, epochs=10, batch_size=32,
          validation_data=(val_data, val_labels))

# or you can train from tf.data dataset
dataset = tf.data.Dataset.from_tensor_slices((data, labels))
dataset = dataset.batch(32)
model.fit(dataset, epochs=10)

# train from tf.data dataset with validation
val_dataset = tf.data.Dataset.from_tensor_slices((val_data, val_labels))
val_dataset = val_dataset.batch(32)
model.fit(dataset, epochs=10,
          validation_data=val_dataset)

# Evaluate and predict
# with Numpy arrays
data_eva = np.random.random((1000, 32))
labels_eva = np.random.random((1000, 10))
model.evaluate(data_eva, labels_eva, batch_size=32)

# with a Dataset
dataset = tf.data.Dataset.from_tensor_slices((data_eva, labels_eva))
dataset = dataset.batch(32)
model.evaluate(dataset)

# predict the output of the last layer
result = model.predict(data, batch_size=32)
print(result.shape)

# Save weights to a TensorFlow Checkpoint file
script_path = os.path.split(os.path.realpath(__file__))[0]
save_to_file = os.path.join(script_path, 'weights', 'my_model')
model.save_weights(save_to_file)

# Restore the model's state,
# this requires a model with the same architecture.
model.load_weights(save_to_file)

# 2. Customize model

inputs = tf.keras.Input(shape=(32,))  # Returns an input placeholder
# A layer instance is callable on a tensor, and returns a tensor.
x = layers.Dense(64, activation='relu')(inputs)
x = layers.Dense(64, activation='relu')(x)
predictions = layers.Dense(10, activation='softmax')(x)

model = tf.keras.Model(inputs=inputs, outputs=predictions)

# The compile step specifies the training configuration.
model.compile(optimizer=tf.keras.optimizers.RMSprop(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(data, labels, batch_size=32, epochs=5)
