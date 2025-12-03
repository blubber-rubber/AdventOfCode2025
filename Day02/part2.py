import time
from functools import lru_cache
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

highest = 0


@lru_cache()
def get_divisors(n):
    divisors = set()
    for d in range(1, round(n ** (1 / 2)) + 2):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return tuple(sorted(divisors, reverse=True))


def is_invalid(x):
    x = str(x)

    m = re.match('^(\d+?)\1+$', x)
    if re.match(r'^(\d+?)\1+$', x):
        return True


ids = [tuple(int(x) for x in both.split('-')) for both in lines[0].split(',')]

som = 0
for l, u in ids:
    print(u / l)
    for i in range(l, u + 1):
        if is_invalid(i):
            som += i

print(som)
print(time.time() - start_time)