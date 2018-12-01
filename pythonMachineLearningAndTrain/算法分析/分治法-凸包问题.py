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


def find(points):
    # 排序
    my_sort(points)
    points[0].flag = 1
    points[points.__len__() - 1].flag = 1
    getTriangleUp(0, points.__len__() - 1, points)
    getTriangleDown(0, points.__len__() - 1, points)
    draw(points)


def getTriangleDown(point_num_1, point_num_n, points):
    # TODO: 寻找位于直线上方或者下方的数据的集合
    points[point_num_1].flag = 1
    points[point_num_n].flag = 1
    points_new_up = []
    points_new_down = []
    a = points[point_num_n].y - points[point_num_1].y
    b = points[point_num_1].x - points[point_num_n].x
    c = (points[point_num_1].x * points[point_num_n].y) - (points[point_num_1].y * points[point_num_n].x)
    for point_ch in range(1, points.__len__() - 1):
        if a * points[point_ch].x + b * points[point_ch].y > c:
            points_new_down.append(points[point_ch])
        else:
            points_new_up.append(points[point_ch])

    # TODO: 两个点连线上方或下方没有点了
    if points_new_up.__len__() == 0 or points_new_down.__len__() == 0:
        return 0
    else:
        # TODO: 寻找距离两个边界点下方最远的点的下标 == max_up_dis_num
        max_down_dis_num = 0
        min_dis = 0
        for down in range(points_new_down.__len__()):
            x_1_max = ((points[point_num_1].x - points_new_down[down].x) ** 2 + (
                    points[point_num_1].y - points_new_down[down].y) ** 2) ** (1 / 2)
            x_n_max = ((points[point_num_n].x - points_new_down[down].x) ** 2 + (
                    points[point_num_n].y - points_new_down[down].y) ** 2) ** (1 / 2)
            dis = x_1_max + x_n_max
            if dis > min_dis:
                min_dis = dis
                max_down_dis_num = down

        max_down_dis_num = getItem(points, points_new_down[max_down_dis_num].x, points_new_down[max_down_dis_num].y)
        getTriangleDown(point_num_1, max_down_dis_num, points)
        getTriangleDown(max_down_dis_num, point_num_n, points)


def draw(points):
    for item in range(points.__len__()):
        if points[item].flag == 1:
            plt.scatter(points[item].x, points[item].y, s=100, color='blue', marker='.')


def getTriangleUp(point_num_1, point_num_n, points):
    # TODO: 寻找位于直线上方或者下方的数据的集合
    points[point_num_1].flag = 1
    points[point_num_n].flag = 1
    points_new_up = []
    points_new_down = []
    a = points[point_num_n].y - points[point_num_1].y
    b = points[point_num_1].x - points[point_num_n].x
    c = (points[point_num_1].x * points[point_num_n].y) - (points[point_num_1].y * points[point_num_n].x)
    for point_ch in range(1, points.__len__() - 1):
        if a * points[point_ch].x + b * points[point_ch].y >= c:
            points_new_down.append(points[point_ch])
        else:
            points_new_up.append(points[point_ch])

    # TODO: 两个点连线上方或下方没有点了
    if points_new_up.__len__() == 0 or points_new_down.__len__() == 0:
        return 0
    else:
        # TODO: 寻找距离两个边界点上方最远的点的下标 == max_up_dis_num
        max_up_dis_num = 0
        min_dis = 0
        for up in range(points_new_up.__len__()):
            x_1_max = ((points[point_num_1].x - points_new_up[up].x) ** 2 + (
                        points[point_num_1].y - points_new_up[up].y) ** 2) ** (
                              1 / 2)
            x_n_max = ((points[point_num_n].x - points_new_up[up].x) ** 2 + (
                        points[point_num_n].y - points_new_up[up].y) ** 2) ** (
                              1 / 2)
            dis = x_1_max + x_n_max
            if dis > min_dis:
                min_dis = dis
                max_up_dis_num = up
        max_up_dis_num = getItem(points, points_new_up[max_up_dis_num].x, points_new_up[max_up_dis_num].y)
        getTriangleUp(point_num_1, max_up_dis_num, points)
        getTriangleUp(max_up_dis_num, point_num_n, points)


def getItem(points, x, y):
    for item in range(points.__len__()):
        if points[item].x == x and points[item].y == y:
            return item
    print('查找下标失败')
    return 0

point_size=30
points = []
create(points)

find(points)

plt.show()
