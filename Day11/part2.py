import time
from collections import defaultdict
from functools import lru_cache

start_time = time.time()


class Node:

    def __init__(self, name, children):
        self.name = name
        self.children = children


with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

nodes = defaultdict(list)
counts = defaultdict(int)

for line in lines:
    name, childs = line.split(': ')
    children = childs.split(' ')
    nodes[name] = children



@lru_cache()
def recursive(current, end):
    if current == end:
        return 1

    som = 0
    for child in nodes[current]:
        som += recursive(child, end)
    return som


print(recursive('svr', 'fft')*recursive('fft', 'dac')*recursive('dac', 'out'))
print(recursive('dac', 'fft') * recursive('svr', 'dac') * recursive('fft', 'out'))

print(time.time() - start_time)
