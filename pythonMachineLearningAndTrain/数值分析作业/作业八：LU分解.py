# 12 * x1 - 3 * x2 + 3 * x3 = 15
# -18 * x1 + 3 * x2 - x3 = -15
# x1 + x2 + x3 = 6

import numpy as np

# A = [[2, 2, 3, 3], [4, 7, 7, 1], [-2, 4, 5, -7]]
A = [[2, 2, 3], [4, 7, 7], [-2, 4, 5]]
B = [[3], [1], [-7]]
n = A.__len__()
m = A[0].__len__()
L = [([0] * 3) for i in range(3)]


# L = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def prevent(expression, i):
    temp = []
    for item_i in range(i - 1, expression.__len__()):
        temp.append(abs(expression[item_i][i - 1]))
    max = 0
    for x in range(temp.__len__()):
        if temp[x] > temp[max]:
            max = x
    max = max + i - 1
    # TODO: 交换
    for item_i in range(expression[max].__len__()):
        t = expression[max][item_i]
        expression[max][item_i] = expression[i - 1][item_i]
        expression[i - 1][item_i] = t


for item_i in range(L.__len__()):
    for item_j in range(L[item_i].__len__()):
        if item_i == item_j:
            L[item_i][item_j] = 1

# TODO: 获得 L 和 U 矩阵
for item_i in range(1, n):  # 1,2

    # TODO: 进行除零的预防
    # prevent(A, item_i)
    for item_j in range(item_i, n):
        div = (A[item_j][item_i - 1] / A[item_i - 1][item_i - 1])
        L[item_j][item_i - 1] = div
        for item_k in range(m):  # 0,1,2,3
            A[item_j][item_k] = A[item_j][item_k] - div * A[item_i - 1][item_k]

u = np.matrix(A)
l = np.matrix(L)
b = np.matrix(B)
print('I am 解奕鹏，1607094128')
d = l.I * b
x = u.I * d
print('x: \n', x)
