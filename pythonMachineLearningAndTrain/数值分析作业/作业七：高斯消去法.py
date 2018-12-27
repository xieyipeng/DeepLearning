# 12 * x1 - 3 * x2 + 3 * x3 = 15
# -18 * x1 + 3 * x2 - x3 = -15
# x1 + x2 + x3 = 6

import numpy as np

expression = [[12, -3, 3, 15], [-18, 3, -1, -15], [1, 1, 1, 6]]
n = expression.__len__()
m = expression[0].__len__()


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


for item_i in range(1, n):  # 1,2
    # TODO: 进行除零的预防
    prevent(expression, item_i)
    for item_j in range(item_i, n):
        div = -(expression[item_j][item_i - 1] / expression[item_i - 1][item_i - 1])
        for item_k in range(m):  # 0,1,2,3
            expression[item_j][item_k] = expression[item_j][item_k] + div * expression[item_i - 1][item_k]

a = np.matrix(expression)
print('I am 解奕鹏，1607094128')
print(a)
