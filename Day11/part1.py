import time
from collections import defaultdict
from functools import lru_cache

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

nodes = defaultdict(list)
counts = defaultdict(int)

for line in lines:
    name, childs = line.split(': ')
    children = childs.split(' ')
    nodes[name] = children


@lru_cache()
def recursive(current):
    if current == 'out':
        return 1

    som = 0
    for child in nodes[current]:
        som += recursive(child)

    return som


print(recursive('you'))

print(time.time() - start_time)
