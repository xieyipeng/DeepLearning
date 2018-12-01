import random
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, flag):
        self.x = x
        self.y = y
        self.flag = flag


def create(points):
    for point in range(point_size):
        point = Point(random.randint(0, 40), random.randint(0, 40), 0)
        points.append(point)
        print(point.x, point.y)
        plt.scatter(point.x, point.y, s=100, color='red', marker='.')
    # point = Point(1, -5, 0)
    # points.append(point)
    # point = Point(5, -10, 0)
    # points.append(point)
    # point = Point(-8, 1, 0)
    # points.append(point)
    # point = Point(-5, 7, 0)
    # points.append(point)
    # point = Point(-2, -9, 0)
    # points.append(point)
    # point = Point(5, 7, 0)
    # points.append(point)
    # point = Point(2, 5, 0)
    # points.append(point)
    # point = Point(-10, 0, 0)
    # points.append(point)
    # for point in range(point_size):
    #     plt.scatter(points[point].x, points[point].y, s=100, color='red', marker='.')


def find(points):
    if points.__sizeof__() == 0:
        print('points为空')
        return 0
    for point_first in range(0, point_size):
        for point_other in range(point_first + 1, point_size):
            # x1,x2为相同的点
            if points[point_first].x == points[point_other].x and points[point_first].y == points[point_other].y:
                continue
            a = points[point_other].y - points[point_first].y
            b = points[point_first].x - points[point_other].x
            c = (points[point_first].x * points[point_other].y) - (points[point_first].y * points[point_other].x)
            flag_big = 0
            flag_small = 0
            for num in range(point_size):
                if num == point_first or num == point_other:
                    continue
                if a * points[num].x + b * points[num].y == c:
                    flag_big = flag_big + 1
                    flag_small = flag_small + 1
                if a * points[num].x + b * points[num].y > c:
                    flag_big = flag_big + 1
                if a * points[num].x + b * points[num].y < c:
                    flag_small = flag_small + 1
            if flag_small == point_size - 2 or flag_big == point_size - 2:
                points[point_first].flag = 1
                points[point_other].flag = 1
                plt.scatter(points[point_first].x, points[point_first].y, s=100, color='b', marker='.')
                plt.scatter(points[point_other].x, points[point_other].y, s=100, color='b', marker='.')


point_size = 30
points = []
create(points)
find(points)

plt.show()
