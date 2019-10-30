# Machine Learning with Python - Ch02

from tensorflow.keras.datasets import mnist
from tensorflow.keras import models, layers
from tensorflow.keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt

# 1. First Example
# Load data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print("train_images.shape:", train_images.shape)
print("train_images.dtype:", train_images.dtype)
print("length of train_labels:", len(train_labels))

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28, )))
network.add(layers.Dense(10, activation='softmax'))
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

train_images = train_images.reshape((train_images.shape[0], 28*28))
train_images = train_images.astype('float32') / 255  # scaling to [0, 1]
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# Preparing the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# training and evaluate
network.fit(train_images, train_labels, epochs=5, batch_size=128)
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)

# 2. tensor

# scalars - 0D tensors
x = np.array(12)
print("x:", x, "x.ndim:", x.ndim)

# vectors - 1D tensors
x = np.array([12, 3, 6, 14])
print("x:", x, "x.ndim:", x.ndim)

# matrices - 2D tensors
x = np.array(
    [[5, 78, 2, 34, 0],
    [6, 79, 3, 35, 1],
    [7, 80, 4, 36, 2]])
print("x:", x, "x.ndim:", x.ndim)

# 3D tensors
x = np.array([[[5, 78, 2, 34, 0],
    [6, 79, 3, 35, 1],
    [7, 80, 4, 36, 2]],
    [[5, 78, 2, 34, 0],
    [6, 79, 3, 35, 1],
    [7, 80, 4, 36, 2]],
    [[5, 78, 2, 34, 0],
    [6, 79, 3, 35, 1],
    [7, 80, 4, 36, 2]]])
print("x:", x, "x.ndim:", x.ndim)

# 3. manipulating tensors in NumPy
my_slice = train_images[10:100]
print("my_slices.shape:", my_slice.shape)

# When considering such a batch tensor, the first axis (axis 0) is called
# the batch axis or batch dimension. This is a term you’ll frequently
# encounter when using Keras and other deep-learning libraries.
batch = train_images[:128]  # batch_size = 128

# broadcast
x = np.random.random((64, 3, 32, 10))
y = np.random.random((32, 10))
z = np.maximum(x, y)
print("z:", z)

