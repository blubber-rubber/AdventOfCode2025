import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

spl = lines.index('')

ranges = [tuple(int(x) for x in line.split('-')) for line in lines[:spl]]
products = [int(line) for line in lines[spl + 1:]]


def intersects(r1, r2):
    if r1 > r2:
        r1, r2 = r2, r1

    if r1[1] >= r2[0]:
        return True


def merge(r1, r2):
    return min(r1[0], r2[0]), max(r1[1], r2[1])


cleaned_ranges = []
for r1 in ranges:
    found = []
    for i, r2 in enumerate(cleaned_ranges):
        if intersects(r1, r2):
            found.append(i)

    if found:
        for f in reversed(found):
            r2 = cleaned_ranges[f]
            del cleaned_ranges[f]
            r1 = merge(r1, r2)

    cleaned_ranges.append(r1)

aantal = 0
for l, u in cleaned_ranges:
    aantal += u - l + 1

print(aantal)
print(time.time() - start_time)
