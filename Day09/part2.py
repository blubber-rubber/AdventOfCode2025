from itertools import combinations
import time

start_time = time.time()

with open('input.txt') as f:
    points = [tuple(int(p) for p in line.rstrip('\n').split(',')) for line in f.readlines()]


def area(c1, c2):
    return (1 + abs(c1[0] - c2[0])) * (1 + abs(c1[1] - c2[1]))


def intersection_of_ranges(r1, r2):
    if r1 > r2:
        r1, r2 = r2, r1

    if r2[0] < r1[1]:
        return max(r1[0], r2[0]), min(r1[1], r2[1])


def is_full_rectangle(intervals, overlaps, top):
    for int_b, int_e in zip(intervals, intervals[1:]):
        lines_above = 0
        for overlap in overlaps:

            if intersection_of_ranges((overlap[0][0], overlap[1][0]), (int_b, int_e)) is not None:
                if overlap[0][1] <= bottom:
                    lines_above += 1
                elif overlap[0][1] < top:
                    return False

        if lines_above % 2 == 0:
            return False

    return True


horizontal_lines = []

for line_begin, line_end in zip(points, points[1:] + points[:1]):
    line = tuple(sorted([line_begin, line_end]))
    if line_begin[1] == line_end[1]:
        horizontal_lines.append(line)

max_area = 0

for c1, c2 in combinations(points, r=2):
    if area(c1, c2) > max_area:
        left = min(c1[0], c2[0])
        right = max(c1[0], c2[0])
        bottom = min(c1[1], c2[1])
        top = max(c1[1], c2[1])

        overlaps = []
        for h_begin, h_end in horizontal_lines:
            overlap = intersection_of_ranges((h_begin[0], h_end[0]), (left, right))

            if overlap is not None and h_end[1] <= top:
                overlaps.append(((overlap[0], h_end[1]), (overlap[1], h_end[1])))

        intervals = list(sorted(set(o[0][0] for o in overlaps))) + [right]

        if is_full_rectangle(intervals, overlaps, top):
            max_area = area(c1, c2)

print(max_area)
print(time.time() - start_time)
