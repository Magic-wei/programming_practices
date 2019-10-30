from tensorflow.keras.datasets import boston_housing
from tensorflow.keras import layers, models

import numpy as np
import matplotlib.pyplot as plt

# import data
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

print("train_data.shape:", train_data.shape)
print("train_targets.shape:", train_targets.shape)
print("test_data.shape:", test_data.shape)
print("test_targets.shape:", test_targets.shape)

# normalization

mean = train_data.mean(axis=0)
std = train_data.std(axis=0)
train_data = (train_data - mean) / std
test_data = (test_data - mean) / std


# model
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model


# trial
model = build_model()
history_predict = []
history_mae = []
for loop in range(train_data.shape[0]):
    new_data = train_data[loop].reshape([1, train_data.shape[1]])
    new_target = train_targets[loop].reshape([1, 1])
    # print("new_data.shape:", new_data.shape)
    # print("new_target.shape:", new_target.shape)
    model.fit(new_data, new_target)
    val_mse, val_mae = model.evaluate(new_data, new_target)
    predict = model.predict(new_data)
    print("predict:", predict)
    history_predict.append(predict[0, 0])
    history_mae.append(val_mae)

plt.figure()
plt.subplot(211)
plt.plot(range(train_data.shape[0]), history_mae, label="MAE")
plt.subplot(212)
plt.plot(range(train_data.shape[0]), history_predict, label="prediction")
plt.plot(range(train_data.shape[0]), train_targets, label="target")
plt.legend()

plt.show()
