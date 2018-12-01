# TODO: 牛顿法：


from sympy import *
import matplotlib.pyplot as plt
import numpy as np


def getValue(x):
    return x ** 2 - 1.5 * x


def getDerivative(dify, x):
    return dify.subs('x', x)


def paintf():
    # TODO: 绘制x轴y轴
    x = np.arange(-1, 4, 0.05)
    y1 = [0 * a for a in x]
    y = np.arange(-1, 4, 0.05)
    x1 = [0 * a for a in y]
    plt.plot(x, y1, '-', color='black')
    plt.plot(x1, y, '-', color='black')

    # TODO: 绘制 y = x ** 2 - 2 * x 的图像
    x = np.arange(0, 3, 0.05)
    y = [getValue(a) for a in x]
    # log2(x)图像
    plt.plot(x, y, '-b', label="y1 = x")
    # label
    plt.legend(loc="lower right")


paintf()

b = 2.5
while abs(getValue(b)) > 0.0001:
    # TODO: 求导函数
    x = symbols("x")
    y = x ** 2 - 1.5 * x
    dify = diff(y, x)
    yValue = getValue(b)
    plt.plot([b, b], [0, yValue], '-r')
    k = getDerivative(dify, b)
    c = getValue(b) - k * b
    b1 = b
    b = -(c / k)
    plt.plot([b, b1], [0, yValue], '-r')

print(b)

plt.show()
