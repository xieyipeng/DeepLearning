import numpy as np
import math
import matplotlib.pyplot as plt


def paintf():
    # TODO: 绘制x轴y轴
    x = np.arange(-1, 3, 0.05)
    y1 = [0 * a for a in x]
    y = np.arange(-5, 2, 0.05)
    x1 = [0 * a for a in y]
    plt.plot(x, y1, '-', color='black')
    plt.plot(x1, y, '-', color='black')

    # TODO: 绘制y=log2(x)的图像
    x = np.arange(0.05, 3, 0.05)
    y = [getY(a) for a in x]
    # log2(x)图像
    plt.plot(x, y, '-b', label="log2(x)")
    # label
    plt.legend(loc="lower right")


def paintPoint():
    # TODO: 标出点a(0.8, 0)，b(1.3, 0)

    plt.scatter(a, 0, s=15, color='blue', marker='.', label='a')
    plt.scatter(b, 0, s=15, color='blue', marker='.', label='b')
    plt.xlabel('x')
    plt.ylabel('y')


def getY(x):
    return x * x * x + 2 * x * x - 3


# TODO: 二分法查找点的坐标
a = 0.1
b = 2.4
paintf()
paintPoint()

media = 0
for num in range(100):
    media = (a + b) / 2
    y = np.arange(-1, 1, 0.05)
    x = [media for a in y]
    plt.plot(x, y, '-b', color='red')
    if math.log(media, 2) == 0:
        print('二分法：media ==', media)
        break
    fa = math.log(a, 2) > 0
    fb = math.log(b, 2) > 0
    if math.log(media, 2) > 0 == fa:
        b = media
    else:
        a = media
    if num == 99:
        print('二分法：media ==', media)

plt.show()

# TODO: 试位法查找点的坐标

a = 0.1
b = 2.4
paintf()
paintPoint()

media = 0

for num in range(100):
    media = (abs(math.log(a, 2)) * b + abs(math.log(b, 2)) * a) / (abs(math.log(b, 2)) + abs(math.log(a, 2)))
    k = (math.log(a, 2) - math.log(b, 2)) / (a - b)
    c = math.log(a, 2) - k * a
    x = np.arange(a, b, 0.05)
    y = [k * a + c for a in x]
    plt.plot(x, y, '-b', color='red')

    if math.log(media, 2) == 0:
        print('试位法：media ==', media)
        break
    fa = math.log(a, 2) > 0
    fb = math.log(b, 2) > 0
    if math.log(media, 2) > 0 == fa:
        b = media
    else:
        a = media
    if num == 99:
        print('试位法：media ==', media)

plt.show()
