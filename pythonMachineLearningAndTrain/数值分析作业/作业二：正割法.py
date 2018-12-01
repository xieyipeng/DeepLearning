# TODO: 正割法：


import matplotlib.pyplot as plt
import numpy as np


def getValue(x):
    return x ** 2 - 1.5 * x


def paintf():
    # TODO: 绘制x轴y轴
    x = np.arange(-1, 4, 0.05)
    y1 = [0 * a for a in x]
    y = np.arange(-1, 4, 0.05)
    x1 = [0 * a for a in y]
    plt.plot(x, y1, '-', color='black')
    plt.plot(x1, y, '-', color='black')

    # TODO: 绘制 y = x ** 2 - 1.5 * x 的图像
    x = np.arange(0, 3, 0.05)
    y = [getValue(a) for a in x]
    # log2(x)图像
    plt.plot(x, y, '-b', label="y = x ** 2 - 1.5 * x")
    # label
    plt.legend(loc="lower right")


paintf()

a = 1
b = 3
c = 0
while abs(getValue(b)) > 0.0001:
    plt.plot([a, b], [getValue(a), getValue(b)], '-r')
    c = b - ((getValue(b) * (a - b)) / (getValue(a) - getValue(b)))
    plt.plot([c, c], [0, getValue(c)], '-r')
    a = b
    b = c
print(c)
plt.show()
