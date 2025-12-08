import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

beams = {lines[0].index('S')}

total = 0

for line in lines[1:]:
    new_beams = set()
    for i, c in enumerate(line):

        if i in beams:
            if c == '.':
                new_beams.add(i)
            else:
                new_beams.add(i - 1)
                new_beams.add(i + 1)
                total += 1

    beams = new_beams

print(total)
print(time.time() - start_time)
