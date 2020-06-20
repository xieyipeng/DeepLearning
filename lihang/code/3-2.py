import numpy as np

T = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
n = T.shape[0]
k = T.shape[1]


# border = np.zeros((n, 2))


class Node(object):
    def __init__(self, item=None):
        self.elem = item
        self.l_child = None
        self.r_child = None


class Tree(object):
    def __init__(self, root=Node()):
        self.root = root

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.l_child is None:
                cur_node.l_child = node
                return
            else:
                queue.append(cur_node.l_child)
            if cur_node.r_child is None:
                cur_node.r_child = node
                return
            else:
                queue.append(cur_node.r_child)

    def __str__(self):
        return self.root.elem


def dfs(node):
    print('dfs')
    if node is None:
        print('none')
        return
    print(node.elem, end=' ')
    dfs(node.l_child)
    dfs(node.r_child)


def build_kd_tree(_node, _depth, m_set):
    global k
    if len(m_set) == 0:
        return
    cut_dim = _depth % k
    len_set = len(m_set)
    mid = len_set // 2
    m_sort_set = sorted(m_set, key=lambda x: x[cut_dim])
    # print(m_sort_set)
    point = m_sort_set[mid]
    # print('choose: ', point)
    _node = Node(point)
    print(_node.elem)
    l_set = []
    r_set = []
    for _i in range(0, mid):
        l_set.append(m_sort_set[_i])
    for _i in range(mid + 1, len(m_set)):
        r_set.append(m_sort_set[_i])
    build_kd_tree(_node.l_child, _depth + 1, l_set)
    build_kd_tree(_node.r_child, _depth + 1, r_set)


if __name__ == '__main__':
    kd_tree = Tree()
    print(type(kd_tree.root))
    build_kd_tree(kd_tree.root, 0, T)
    dfs(kd_tree.root)
