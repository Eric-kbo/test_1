# import tensorflow as tf
# import tensorflow.compat.v1 as tf
# hello = tf.constant('heelos')
# sess = tf.Session()
# print(sess.run(hello))
# # print("hello")

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print('GPU',tf.test.is_gpu_available())


aa = tf.constant('hello')

a = tf.constant(2.0)
b = tf.constant(4.0)
print(aa)

print(a+b)

print(tf.__version__)