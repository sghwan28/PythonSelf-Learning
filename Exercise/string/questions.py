def dis(c1: tuple, c2: tuple):
    return ((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2) ** 0.5


print(dis((2, 2), (0, 0)))