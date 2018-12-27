import random
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, flag):
        self.x = x
        self.y = y
        self.flag = flag


def create(points):
    for point in range(point_size):
        point_add = Point(random.randint(0, 40), random.randint(0, 40), 0)
        if points.__len__() == 0:
            points.append(point_add)
        else:
            is_add = 0
            while is_add == 0:
                for point_check in range(points.__len__()):
                    if points[point_check].x != point_add.x or points[point_check].y != point_add.y:
                        points.append(point_add)
                        is_add = 1
                        break
                    else:
                        point_add = Point(random.randint(0, 40), random.randint(0, 40), 0)
        plt.scatter(point_add.x, point_add.y, s=100, color='red', marker='.')


def my_sort(points):
    for point_i in range(0, points.__len__()):
        for point_j in range(point_i + 1, points.__len__()):
            if points[point_i].x > points[point_j].x:
                temp = points[point_i]
                points[point_i] = points[point_j]
                points[point_j] = temp


def getItem(x, y):
    global points
    for item in range(points.__len__()):
        if points[item].x == x and points[item].y == y:
            return item
    print('查找下标失败')
    return 0


def find(points):
    if points.__len__() == 1:
        return [999, 0, 0]
    elif points.__len__() == 2:
        return [((points[1].x - points[0].x) ** 2 + (points[1].y - points[0].y) ** 2) ** (
                1 / 2), getItem(points[0].x, points[0].y), getItem(points[1].x, points[1].y)]
    else:
        my_sort(points)
        media = int(points.__len__() / 2)
        left = points[0:media]
        right = points[-media:]
        min_left = find(left)
        min_right = find(right)
        min_d = 0
        min_a = 0
        min_b = 0
        if min_left[0] < min_right[0]:
            min_d = min_left[0]
            min_a = min_left[1]
            min_b = min_left[2]
        else:
            min_d = min_right[0]
            min_a = min_right[1]
            min_b = min_right[2]

        area_left = points[media].x - min_d
        area_right = points[media].x + min_d
        resoult_array = []
        for item in range(points.__len__()):
            if area_left <= points[item].x <= area_right:
                resoult_array.append(points[item])
        # TODO: 蛮力法查找最近对
        for point_i in range(0, resoult_array.__len__() - 1):
            for point_j in range(point_i + 1, resoult_array.__len__() - 1):
                dis = ((resoult_array[point_j].x - resoult_array[point_i].x) ** 2 + (
                        resoult_array[point_j].y - resoult_array[point_i].y) ** 2) ** (
                              1 / 2)
                # global min_d, min_a, min_b
                if dis < min_d:
                    min_d = dis
                    min_a = getItem(resoult_array[point_i].x, resoult_array[point_i].y)
                    min_b = getItem(resoult_array[point_j].x, resoult_array[point_j].y)
        return [min_d, min_a, min_b]


point_size = 10
points = []
create(points)
r = find(points)
print('最短距离：', r[0])
plt.plot([points[r[1]].x, points[r[2]].x], [points[r[1]].y, points[r[2]].y], '-b')
plt.show()
