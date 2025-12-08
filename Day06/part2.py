import time
import re
import math

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n')+' '*10 for line in f.readlines()]

spaces = 0
total = 0
for m in re.finditer('[^\s]\s*', lines[-1], ):
    s = len(m.group())
    data = [line[spaces:spaces + s] for line in lines[:-1]]

    op = m.group()[0]

    transpose = [''.join(d[j] for d in data).strip(' ') for j in range(len(data[0]))]

    if op == '+':
        total += sum(int(x) for x in transpose if x != '')
    else:
        total += math.prod(int(x) for x in transpose if x != '')
    spaces+=s

print(total)
print(time.time() - start_time)
