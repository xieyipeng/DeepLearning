# nand_gate
import numpy as np
from add_gate import AND
from nand_gate import NAND
from or_gate import OR


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


if __name__ == '__main__':
    for i in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = XOR(i[0], i[1])
        print(str(i) + " -> " + str(y))
