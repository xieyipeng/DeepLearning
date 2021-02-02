import sys
import os

sys.path.append(os.pardir)
from dataset.minist import load_mnist
import pickle
import numpy as np
from commom.functions import sigmoid, softmax
from PIL import Image


def get_data():
    """
    获取数据
    """
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    """
    加载网络
    """
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    """
    预测
    """
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3

    y = softmax(a3)
    return y


if __name__ == '__main__':
    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0

    # for i in range(len(x)):
    #     y = predict(network, x[i])
    #     p = np.argmax(y)  # 获取概率最高的元素索引
    #     if p == t[i]:
    #         accuracy_cnt += 1

    batch_size = 100
    for i in range(0, len(x), batch_size):
        x_batch = x[i:i + batch_size]
        y_batch = predict(network, x_batch)
        p = np.argmax(y_batch, axis=1)
        accuracy_cnt += np.sum(p == t[i:i + batch_size])

    print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
