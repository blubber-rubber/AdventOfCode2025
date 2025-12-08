import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

rows = [[x for x in line.split(' ') if x != ''] for line in lines]

total = 0

for a, b, c,d, op in zip(*rows):
    if op == '+':
        total += int(a) + int(b) + int(c) + int(d)
    else:
        total += int(a) * int(b) * int(c) * int(d)
print(total)
print(time.time() - start_time)
