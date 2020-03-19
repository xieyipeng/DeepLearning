# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Modify Time      @Author
 ---------        -------
 2020/3/11       xieyipeng
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 
"""

import tensorflow as tf

w = tf.Variable(0, dtype=tf.float32)
cost = tf.add(tf.add(w ** 2, tf.multiply(-10., w)), 25)
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
init = tf.compat.v1.global_variables_initializer()
session = tf.compat.v1.Session()
session.run(init)
print(session.run(w))
