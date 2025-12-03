import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

N = 100

start = 50
aantal = 0

for line in lines:
    start = ((-1) ** (line[0] == 'L') * int(line[1:])+start)%N

    if start == 0:
        aantal += 1

print(aantal)
print(time.time() - start_time)
