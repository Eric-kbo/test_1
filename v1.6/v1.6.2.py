import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
mint = tf.keras.datasets.mnist
data = pd.read_csv('../datas/v1.61.csv')

x = data.Education
y = data.Income

model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(1, input_shape=(1,)))

model.summary()

model.compile(optimizer='adam', loss='mse')

history = model.fit(x, y, epochs=5000)

model.predict(x)
model.predict(pd.Series([20]))

# plt.scatter(data.Education,data.Income)

# print(data)
