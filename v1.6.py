from pyexpat import model
import numpy
import tensorflow as tf

print(tf.__path__)

# model.compile()
mint = tf.keras.datasets.mnist
(x_,y_),(x_1,y_1) = mint.load_data()

print(x_)
