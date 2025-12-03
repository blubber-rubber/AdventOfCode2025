import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def is_invalid(x):
    x = str(x)

    if len(x) % 2 == 1:
        return False

    return x[:len(x) // 2] == x[len(x) // 2:]


ids = lines[0].split(',')

som = 0

for both in ids:
    l, u = [int(x) for x in both.split('-')]
    for i in range(l, u + 1):
        if is_invalid(i):
            som += i

print(som)
print(time.time() - start_time)
