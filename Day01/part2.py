import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

N = 100

start = 50
aantal = 0

for line in lines:
    direction = line[0]
    number = int(line[1:])

    full_rotations = number // N
    aantal += full_rotations
    number = number % 100

    if start != 0 and ((direction == 'L' and number >= start) or (direction == 'R' and number >= 100 - start)):
        aantal += 1



    start = ((-1) ** (direction == 'L') * number + start) % N

print(aantal)
print(time.time() - start_time)
