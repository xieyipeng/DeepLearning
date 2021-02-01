# add gate
import numpy as np


def AND1(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1


if __name__ == '__main__':
    for i in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = AND(i[0], i[1])
        print(str(i) + " -> " + str(y))
