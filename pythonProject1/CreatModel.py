from keras.models import Sequential
from keras.layers import LSTM
import numpy as np

x_train = np.random.rand(1000, 10) # Временное решение до создания корректного Dataset
y_train = np.random.rand(1000,10) # Временное решение до создания корректного Dataset

model = Sequential()
model.add(LSTM(units=64, activation='relu', input_dim=10))
model.add(LSTM(units=64, activation='relu'))
model.add(LSTM(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=10, batch_size=32)
model.save('model_name.h5')
print('Модель сохранена')