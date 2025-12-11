from itertools import combinations
import time

start_time = time.time()

with open('input.txt') as f:
    points = [tuple(int(p) for p in line.rstrip('\n').split(',')) for line in f.readlines()]


def area(c1, c2):
    return (1 + abs(c1[0] - c2[0])) * (1 + abs(c1[1] - c2[1]))


max_area = 0

for c1, c2 in combinations(points, r=2):
    max_area = max(max_area, area(c1, c2))

print(max_area)
print(time.time() - start_time)
