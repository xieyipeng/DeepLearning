import numpy as np
import matplotlib.pyplot as plt

x = [-1, 0, 1, 2]
ca = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(0, 9):
    if i < 2:
        ca[i][0] = x[i] ** 2
        ca[i][1] = x[i]
        ca[i][2] = 1
    if i >= 2 and i <= 3:
        ca[i][3] = x[i - 1] ** 2
        ca[i][4] = x[i - 1]
        ca[i][5] = 1
    if i >= 4 and i <= 5:
        ca[i][6] = x[i - 2] ** 2
        ca[i][7] = x[i - 2]
        ca[i][8] = 1
    if i == 6:
        ca[i][0] = 2 * x[1]
        ca[i][1] = 1
        ca[i][3] = -2 * x[1]
        ca[i][4] = -1
    if i == 7:
        ca[i][3] = 2 * x[2]
        ca[i][4] = 1
        ca[i][6] = -2 * x[2]
        ca[i][7] = -1
    if i == 8:
        ca[i][0] = 1

re = [[0], [0.5], [0.5], [2], [2], [1.5], [0], [0], [0]]
ca = np.mat(ca)
re = np.mat(re)
ca = ca.I
y = ca * re

print(y)

x1 = np.arange(-1, 0, 0.05)
y1 = [y[0, 0] * x * x + y[1, 0] * x + y[2, 0] for x in x1]

x2 = np.arange(0, 1, 0.05)
y2 = [y[3, 0] * x * x + y[4, 0] * x + y[5, 0] for x in x2]

x3 = np.arange(1, 2, 0.05)
y3 = [y[6, 0] * x * x + y[7, 0] * x + y[8, 0] for x in x3]


plt.plot(x1, y1, '-b')
plt.plot(x2, y2, '-c')
plt.plot(x3, y3, '-r')
plt.show()
