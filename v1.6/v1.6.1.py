import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
mint = tf.keras.datasets.mnist
data = pd.read_csv('../datas/v1.61.csv')


plt.scatter(data.Education,data.Income)

print(data)