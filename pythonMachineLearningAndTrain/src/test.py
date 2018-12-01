import numpy as np
import matplotlib.pyplot as plt


def f(x):
    cost = x
    return cost


def dichotomy(a, b, c):
    x1 = []
    y2 = []
    mid = 0.1
    i = 0
    while i < 50:
        mid = (b + a) / 2
        x1.append(mid)
        y2.append(f(mid))
        print(mid)
        i = i + 1
        if f(mid) == 0:
            return mid
        if f(a) * f(mid) < 0:
            b = mid
            print(mid)
        else:
            a = mid
            print(mid)

    print(x1)
    print(y2)
    plt.plot(x1, y2, 'o')
    return mid


print(dichotomy(-9, 10, 0.6))
a = np.linspace(0, 10, 100)
x = []
y = []
for i in a:
    x.append(i)
    y.append(f(i))
plt.plot(x, y)
plt.show()
