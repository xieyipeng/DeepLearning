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
        plt.scatter(point.x, point.y, s=100, color='red', marker='.')


def find(points):
    max_num = 99999
    point_a = 0
    point_b = 0
    for point_i in range(0, point_size - 1):
        for point_j in range(point_i+1, point_size):
            dis = ((points[point_j].x - points[point_i].x) ** 2 + (points[point_j].y - points[point_i].y) ** 2) ** (
                    1 / 2)
            print(dis)
            if dis < max_num:
                max_num = dis
                point_a = point_i
                point_b = point_j
    plt.scatter(points[point_a].x, points[point_a].y, s=100, color='b', marker='.')
    plt.scatter(points[point_b].x, points[point_b].y, s=100, color='b', marker='.')


point_size = 10
points = []
create(points)
find(points)
plt.show()
