import time
from collections import Counter

import numpy as np
from scipy.spatial.distance import cdist

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


class Node:

    def __init__(self, coords):
        self.x, self.y, self.z = coords

        self.parent = None
        self.children = []
        self.n_children = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_coords(self):
        return self.x, self.y, self.z

    def __hash__(self):
        return self.get_coords().__hash__()

    def set_parent(self, node):
        if self != node:
            self.parent = node
            node.add_child(self)
            node.n_children += self.n_children + 1

    def add_child(self, node):
        self.children.append(node)

    def get_root(self):
        if self.parent is None:
            return self
        return self.parent.get_root()

    def distance_to_p(self, node, p=2):
        return ((self.x - node.x) ** p + (self.y - node.y) ** p + (self.z - node.z) ** p)


points = []
for line in lines:
    points.append(Node(tuple(int(x) for x in line.split(','))))

coords = np.loadtxt("input.txt", delimiter=",")
# Pairwise Euclidean distance matrix (N × N)
D = cdist(coords, coords)

distances = []
for i, p1 in enumerate(points):
    for j, p2 in enumerate(points[i + 1:]):
        distances.append((D[i][i + j + 1], p1, p2))

distances.sort()



for d, p1, p2 in distances[:1000]:
    r1 = p1.get_root()
    r2 = p2.get_root()

    r1.set_parent(r2)

roots = list(sorted(set(p.get_root() for p in points), key=lambda r: r.n_children, reverse=True))

a, b, c = [1 + r.n_children for r in roots[:3]]

print(a * b * c)

print(time.time() - start_time)
