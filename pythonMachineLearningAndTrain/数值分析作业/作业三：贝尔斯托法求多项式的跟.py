r = -1
s = -1
d_r = -1
d_s = -1
max_power = 5
fi = 0.01

a = [1.25, -3.875, 2.15, 2.75, -3.5, 1]
b = [0, 0, 0, 0, 0, 0]
c = [0, 0, 0, 0, 0, 0]


def getValue(x):
    return a[5] * x ** 5 - a[4] * (x ** 4) + a[3] * (x ** 3) + a[2] * (x ** 2) - a[1] * x + a[0]


def changeBi(bi):
    if bi == max_power:
        return a[max_power]
    elif bi == max_power - 1:
        return a[max_power - 1] + r * b[max_power]
    else:
        return a[bi] + r * b[bi + 1] + s * b[bi + 2]


def changeCi(ci):
    if ci == max_power:
        return b[max_power]
    elif ci == max_power - 1:
        return b[max_power - 1] + r * c[max_power]
    else:
        return b[ci] + r * c[ci + 1] + s * c[ci + 2]


def getValues2(r_r, r_s):
    r_a, r_b, r_c = 1, -r_r, -r_s
    dt = r_b * r_b - 4 * r_a * r_c
    return (-r_b + dt ** (1 / 2)) / (2 * r_a), (-r_b - dt ** (1 / 2)) / (2 * r_a)


while (d_r / r) > fi or (d_s / s) > fi:
    # TODO: 5次项第一次除以二次项，改变b的值
    for x in reversed(range(max_power + 1)):
        b[x] = changeBi(x)

    # TODO: 5次项第一次除以二次项，改变c的值
    for x in reversed(range(max_power + 1)):
        c[x] = changeCi(x)

    d_r = ((c[2] * b[1] - b[0] * c[3]) / (c[1] * c[3] - c[2] * c[2]))
    d_s = (c[1] * b[1] - b[0] * c[2]) / (c[2] * c[2] - c[3] * c[1])
    r = r + d_r
    s = s + d_s

print(getValues2(r, s))

d_r, d_s = r, s
max_power = 3
a = [b[2], b[3], b[4], b[5]]
b = [0, 0, 0, 0]
c = [0, 0, 0, 0]

while (d_r / r) > fi or (d_s / s) > fi:
    # TODO: 5次项第二次除以二次项，改变b的值
    for x in reversed(range(max_power + 1)):
        b[x] = changeBi(x)

    # TODO: 5次项第二次除以二次项，改变c的值
    for x in reversed(range(max_power + 1)):
        c[x] = changeCi(x)
    d_r = ((c[2] * b[1] - b[0] * c[3]) / (c[1] * c[3] - c[2] * c[2]))
    d_s = (c[1] * b[1] - b[0] * c[2]) / (c[2] * c[2] - c[3] * c[1])
    r = r + d_r
    s = s + d_s

print(getValues2(r, s))

d_r, d_s = r, s
a = [b[2], b[3]]
b = [0, 0]
c = [0, 0]

print(-(a[0]/a[1]))
