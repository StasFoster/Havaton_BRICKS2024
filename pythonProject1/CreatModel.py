import tensorflow
import keras
import numpy as np

x_train = []
y_train = []
with open("Dataset/Train/vehicle.params") as f:
    list_ = f.readlines()
    for i in range(len(list_) - 30):
        x_train.append(list_[i:i+30])
with open("Dataset/Valid/vehicle.params") as f:
    list_ = f.readlines()
    for i in range(len(list_) - 30):
        y_train.append(list_[i:i+30])

model = keras.Sequential()
model.add(keras.LSTM(units=64, activation='relu', input_dim=10))
model.add(keras.LSTM(units=64, activation='relu'))
model.add(keras.LSTM(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=10, batch_size=32)
model.save('model_name.h5')
print('Модель сохранена')