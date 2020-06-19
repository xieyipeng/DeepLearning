import numpy as np


def creatDataSet():
    group = np.array([[3, 3], [4, 3], [1, 1]])
    label = [1, 1, -1]
    return group, label


def update(x, y, i):
    global a, b, G
    a[i] += 1
    b = b + y


def cal(x, label, row):
    print('row: ',row)
    global a, b, G
    result = 0
    for i in range(len(G[row])):
        result += label[i] * a[i] * G[row][i]
    result += b
    result *= label[row]
    return result


def perceptron_func(group, label):
    global a, b, G
    isFind = False
    n = group.shape[0]
    a = np.zeros(n, dtype=np.int)
    b = 0
    G = np.zeros((n, n), dtype=np.int)
    print(group)

    # 计算Gam矩阵
    for i in range(n):
        for j in range(n):
            G[i][j] = group[i][0] * group[j][0] + group[i][1] * group[j][1]
    print(G)

    while isFind == False:
        for i in range(n):
            if cal(group[i], label, i) <= 0:
                update(group[i], label[i], i)
                print(a, b)
                break
            elif i == n - 1:
                print(a, b)
                isFind = True


g, l = creatDataSet()
perceptron_func(g, l)
