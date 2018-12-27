import numpy as np
import matplotlib.pyplot as plt

x = [0.0, 0.2, 0.4, 0.6, 0.8]
y = [0.9, 1.9, 2.8, 3.3, 4.2]

n = 0
if x.__len__() == y.__len__():
    n = x.__len__()
else:
    print('x和y的大小不一样')

x_all = 0
for item in range(x.__len__()):
    x_all = x_all + x[item]
    plt.scatter(x[item], y[item], s=100, color='red', marker='.')

x_squire_all = 0
for item in range(x.__len__()):
    x_squire_all = x_squire_all + (x[item]) ** 2

y_all = 0
for item in range(y.__len__()):
    y_all = y_all + y[item]

x_y_multiply = 0
for item in range(x.__len__()):
    x_y_multiply = x_y_multiply + x[item] * y[item]

matrix_a = np.mat([[n, x_all], [x_all, x_squire_all]])
matrix_b = np.mat([[y_all], [x_y_multiply]])
matrix_a = matrix_a.I

resoult = matrix_a * matrix_b

a = -0.4
b = 1
plt.plot([a, b], [resoult.item(0, 0) + resoult.item(1, 0) * a, resoult.item(0, 0) + resoult.item(1, 0) * b], '-b', )

plt.show()
