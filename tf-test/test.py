# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Modify Time      @Author
 ---------        -------
 2020/3/11       xieyipeng
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 
"""

import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()


def initialize_parameters():
    """
    初始化权值矩阵，这里我们把权值矩阵硬编码：
    W1 : [4, 4, 3, 8]
    W2 : [2, 2, 8, 16]

    返回：
        包含了tensor类型的W1、W2的字典
    """
    tf.set_random_seed(1)

    W1 = tf.get_variable("W1", [4, 4, 3, 8], initializer=tf.contrib.layers.xavier_initializer(seed=0))
    W2 = tf.get_variable("W2", [2, 2, 8, 16], initializer=tf.contrib.layers.xavier_initializer(seed=0))

    parameters = {"W1": W1,
                  "W2": W2}

    return parameters


tf.reset_default_graph()
with tf.Session() as sess_test:
    parameters = initialize_parameters()
    init = tf.global_variables_initializer()
    sess_test.run(init)
    print("W1 = " + str(parameters["W1"].eval()[1, 1, 1]))
    print("W2 = " + str(parameters["W2"].eval()[1, 1, 1]))

    sess_test.close()
