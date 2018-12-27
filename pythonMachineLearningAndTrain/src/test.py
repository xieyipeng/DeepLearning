import numpy as np
import matplotlib.pyplot as plt

a = np.array([[3, 4.5, 7, 9], [2.5, 1, 2.5, 0.5]])    # a[0]存放x, a[1]存放f(x)    # 利用maxsize手动初始化

maxsize = 3*(a[0].size-1)-1

b = np.zeros((maxsize, maxsize+1))    # 系数矩阵
result = np.zeros(maxsize)    # 未知数矩阵
c = np.zeros(maxsize)    # 常数项矩阵
# 系数矩阵：
# [[x1（0）, 1, 0, 0, 0, 0, 0, 0],
#  [x2（1）, 1, 0, 0, 0, 0, 0, 0],
#  [0, 0, x2^2（1）, x2（1）, 1, 0, 0, 0],
#  [0, 0, x3^2（4）, x3（2）, 1, 0, 0, 0],
#  [0, 0, 0, 0, 0, x3^2（4）, x3（2）, 1],
#  [0, 0, 0, 0, 0, x4^2（16）, x4（4）, 1],
#  [1, 0, -2x2（-2）, -1, 0, 0, 0, 0],
#  [0, 0, 2x3（4）, 1, 0, -2x3（-4）, -1, 0],]

# 二次系数
i = 2
j = 2
k = 1
while i < maxsize-2 and j < maxsize:
    b[i][j] = a[0][k]*a[0][k]
    b[i+1][j] = a[0][k+1]*a[0][k+1]
    i = i+2
    j = j+3
    k = k+1
# 一次系数
i = 0
j = 0
k = 0
while i < maxsize-2 and j < maxsize:
    b[i][j] = a[0][k]
    b[i+1][j] = a[0][k+1]
    i = i+2
    j = j+3
    k = k+1
# 0次系数
i = 0
j = 1
while i < maxsize-2 and j < maxsize:
    b[i][j] = 1
    b[i+1][j] = 1
    i = i+2
    j = j+3
# 减去的两行
b[6][0] = 1
b[6][2] = -2*a[0][1]
b[6][3] = -1
b[7][2] = 2*a[0][2]
b[7][3] = 1
b[7][5] = -2*a[0][2]
b[7][6] = -1

# [f(x1), f(x2), f(x2), f(x3), f(x3), f(x4), 0, 0]
c = [a[1][0], a[1][1], a[1][1], a[1][2], a[1][2], a[1][3], 0, 0]
for i in range(maxsize):
    b[i][maxsize] = c[i]

print('********************原始矩阵************************')
print(b)

# 未知数矩阵
# s = [b1, c1, a2, b2, c2,, a3, b3, c3 ]

# 系数矩阵转换为上三角阵
print('********************行交换/列主元当前最大************************')
for j in range(maxsize):
    for s in range(j+1, maxsize, 1):
        if b[s][j] > b[j][j]:
            for t in range(maxsize+1):
                b[j][t], b[s][t] = b[s][t], b[j][t]
print(b)

print('********************行交换/除零************************')
for j in range(maxsize):
    if b[j][j] == 0:
        for s in range(maxsize):
            if b[s][j] != 0 and b[j][s] != 0:
                for t in range(maxsize+1):
                    b[j][t], b[s][t] = b[s][t], b[j][t]
print(b)

print('********************列交换/除零************************')
exchange = np.zeros((maxsize, maxsize))    # 记录所交换的列
for j in range(maxsize):
    if b[j][j] == 0:
        for s in range(maxsize):
            if b[j][s] != 0:
                for t in range(maxsize):    # 交换列
                    b[t][j], b[t][s] = b[t][s], b[t][j]     # s,j列进行了交换，则结果集相应行应该进行交换
                exchange[j][s] = 1    # 记录所交换的列
print(b)

print('********************上三角阵************************')
for j in range(maxsize):
    for i in range(j+1, maxsize, 1):
        times = b[i][j]/b[j][j]
        for t in range(maxsize+1):
            b[i][t] = b[i][t]-times*b[j][t]
print(b)

# 常数项矩阵
print('********************常数项************************')
for i in range(maxsize):
    c[i] = b[i][maxsize]
print(c)

# 计算各项未知数s[]
for i in range(maxsize-1, -1, -1):
    minus = 0
    for j in range(maxsize-1, i, -1):
        minus = minus + b[i][j]*result[j]
    result[i] = (c[i]-minus)/b[i][i]
print('********************未知数解集/交换前************************')
print(result)
for i in range(maxsize):    # 相对与之前的列交换进行结果集的行交换
    for j in range(maxsize):    # 上面的exchange记录阵是对称的， 所以在此防止重复交换
        if exchange[i][j] == 1:
            result[i], result[j] = result[j], result[i]    # 结果集行交换
print('********************未知数解集/交换后************************')
print(result)


'''函数定义'''


def f0(x):
    return '无法判断'


def f1(x):
    return result[0] * x + result[1]


def f2(x):
    return result[2] * x * x + result[3] * x + result[4]


def f3(x):
    return result[5] * x * x + result[6] * x + result[7]


# 输入判断点，给出判断结果
init = float(input('请输入你的判断点(比如5)：'))
if init < a[0][0] or init > a[0][3]:
    out = f0(init)
elif init <= a[0][1]:
    out = f1(init)
elif init <= a[0][2]:
    out = f2(init)
elif init <= a[0][3]:
    out = f3(init)
print('判断结果：', out)
print('1607094104+王效丫')
# 绘图
plt.figure(1)
for i in range(a[0].size):
    plt.scatter(a[0][i], a[1][i], s=10, c='r', alpha=1, marker='o')    # 在图中标出已知点
plt.scatter(init, out, s=10, c='r', alpha=1, marker='o')    # 图中标出所求点
x1 = np.linspace(a[0][0], a[0][1], 100)
plt.plot(x1, f1(x1))
x2 = np.linspace(a[0][1], a[0][2], 100)
plt.plot(x2, f2(x2))
x3 = np.linspace(a[0][2], a[0][3], 100)
plt.plot(x3, f3(x3))
plt.show()
