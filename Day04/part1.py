import time

start_time = time.time()

with open('input.txt') as f:
    grid = [line.rstrip('\n') for line in f.readlines()]

dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

spots =  []
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        aantal = 0
        if c == '@':
            for dy, dx in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < len(line) and 0 <= ny < len(grid):
                    aantal += grid[ny][nx] == '.'
                else:
                    aantal += 1

            if aantal>4:
                spots.append((y,x))

print(len(spots))
print(time.time() - start_time)
