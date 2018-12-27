import numpy as np
import matplotlib.pyplot as plt

x = [0.4, 0.55, 0.65, 0.8, 0.9, 1.05]
y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]
max_power = x.__len__()
print('I am 解奕鹏，1607094128')
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


print(matrix)
print(getValue(0.596))

paint_x = np.arange(-20, 20, 0.01)
paint_y = [getValue(x) for x in paint_x]

plt.plot(paint_x, paint_y, '-b')
plt.show()
