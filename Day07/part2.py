import time
from functools import lru_cache

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

start_pos = (0, lines[0].index('S'))


@lru_cache()
def recursive(current_pos):
    y, x = current_pos

    if y == len(lines):
        return 1

    c = lines[y][x]

    if c != '^':
        return recursive((y + 1, x))

    return recursive((y, x - 1)) + recursive((y, x + 1))




print(recursive(start_pos))
print(time.time() - start_time)
