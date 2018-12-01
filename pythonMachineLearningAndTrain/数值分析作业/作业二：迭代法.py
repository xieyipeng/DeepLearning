# TODO: 迭代法 x = cmath.sqrt(2x)

import math
import matplotlib.pyplot as plt
import numpy as np


def getValueY1(x):
    return x


def getValueY2(x):
    return math.sqrt(2 * x)


def paintf():
    # TODO: 绘制x轴y轴
    x = np.arange(-0.5, 3, 0.05)
    y1 = [0 * a for a in x]
    y = np.arange(-0.5, 3, 0.05)
    x1 = [0 * a for a in y]
    plt.plot(x, y1, '-', color='black')
    plt.plot(x1, y, '-', color='black')

    # TODO: 绘制 y1 = x 的图像
    x = np.arange(0, 3, 0.05)
    y = [getValueY1(a) for a in x]
    # log2(x)图像
    plt.plot(x, y, '-c', label="y1 = x")
    # label
    plt.legend(loc="lower right")

    # TODO: 绘制 y2 = math.sqrt(2x) 的图像
    x = np.arange(0, 3, 0.05)
    y = [getValueY2(a) for a in x]
    # log2(x)图像
    plt.plot(x, y, '-b', label="y2 = math.sqrt(2x)")
    # label
    plt.legend(loc="lower right")


paintf()

# TODO: 临近点：b=1.1
b = 1.1
res1 = 0
res2 = 0
while abs(getValueY1(b) - getValueY2(b)) > 0.0001:
    yValue = getValueY2(b)
    plt.plot([b, yValue], [yValue, yValue], '-r')
    b = yValue
    x3 = yValue
    y3 = getValueY2(x3)
    plt.plot([x3, yValue], [y3, yValue], '-r')
    print('b ==', b)

plt.show()
