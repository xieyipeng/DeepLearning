# -*- encoding: utf-8 -*-
"""
@File    :   wuenda_tf.py
@Time    :   2020/3/19
@Author  :   xieyipeng
@Review  :   
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 
"""
import numpy as np
import tensorflow as tf

coefficients = np.array([[1.], [-20.], [100.]])

w = tf.Variable(0, dtype=tf.float32)
x = tf.compat.v1.placeholder(tf.float32, [3, 1])

# TODO: cost function
# cost = tf.add(tf.add(w ** 2, tf.multiply(-10., w)), 25)
# cost = w ** 2 - 10 * w + 25
cost = x[0][0] * w ** 2 + x[1][0] * w + x[2][0]
train = tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.compat.v1.global_variables_initializer()
session = tf.compat.v1.Session()
session.run(init)

session.run(train, feed_dict={x: coefficients})
print(session.run(w))

# session.run(train)
# print(session.run(w))

for i in range(1000):
    session.run(train, feed_dict={x: coefficients})

print(session.run(w))
