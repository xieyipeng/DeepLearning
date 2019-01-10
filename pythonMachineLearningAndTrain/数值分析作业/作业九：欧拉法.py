import numpy as np
import matplotlib.pyplot as plt

# TODO: y0 == 1
# TODO: y'=y-((2*x)/y)
h = 0.1
x = np.arange(0, 1.1, 0.1)
y = ([0] * x.__len__())
print('I am 解奕鹏，1607094128')
y[0] = 1
for item in range(x.__len__()):
    if item >= 1:
        y[item] = y[item - 1] + h * (y[item - 1] - ((2 * x[item]) / y[item - 1]))

# 牛顿插值画出图像
matrix = [[0] * (x.__len__() - 1) for i in range(y.__len__() - 1)]
for item_i in range(x.__len__() - 1):
    for item_j in range(x.__len__() - 1 - item_i):
        if item_i == 0:
            poor = item_i + 1
            matrix[item_i][item_j] = (y[item_j + poor] - y[item_j]) / (x[item_j + poor] - x[item_j])
        else:
            poor = item_i + 1
            matrix[item_i][item_j] = (matrix[item_i - 1][item_j + 1] - matrix[item_i - 1][item_j]) / (
                    x[item_j + poor] - x[item_j])


def getValue(num):
    result = 0
    for item in range(x.__len__()):
        if item == 0:
            result = result + y[0]
        else:
            temp = 1
            for item_m in range(item):
                temp = temp * (num - x[item_m])
            result = result + matrix[item - 1][item - 1] * temp
    return result


paint_x = np.arange(0, 1, 0.01)
paint_y = [getValue(x) for x in paint_x]

plt.plot(paint_x, paint_y, '-b')
plt.show()
