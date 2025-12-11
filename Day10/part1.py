import time
import re
import heapq

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def get_joltage(button, joltages):
    return sum(joltages[l] for l in button)


def get_distance(goal, buttons, joltages):
    stack = [(0, tuple(0 for _ in goal))]

    while stack:
        cd, current = heapq.heappop(stack)

        for button in buttons:
            jolt = get_joltage(button, joltages)
            lights = [c for c in current]
            for light in button:
                lights[light] = 1 - lights[light]

            lights = tuple(lights)
            nd = 1 + cd

            if lights == goal:
                return nd

            heapq.heappush(stack,(nd, lights))


total = 0
for i,line in enumerate(lines):
    goal, buttons, joltages = re.match('^\[(.*)] (.*) \{(.*)}$', line).groups()

    goal = tuple(1 if x == '#' else 0 for x in goal)
    buttons = [tuple(int(x) for x in g.groups()[0].split(',')) for g in re.finditer('\(([^)]*)\)', buttons)]
    joltages = tuple(int(x) for x in joltages.split(','))

    total+= get_distance(goal,buttons,joltages)
    print(i+1, 'done')


print(total)
print(time.time() - start_time)
