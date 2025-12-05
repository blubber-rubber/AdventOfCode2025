import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

spl = lines.index('')

ranges = [tuple(int(x) for x in line.split('-')) for line in lines[:spl]]
products = [int(line) for line in lines[spl + 1:]]

print(sum(any(l <= p <= u for l, u in ranges) for p in products))
print(time.time() - start_time)
