import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

result = 0
for line in lines:
    found = False
    find = 9
    while not found:
        if str(find) in line:
            i = line.index(str(find))

            if len(line) - 1 > i:
                found = True
                line2 = list(int(c) for c in line[i + 1:])
                find2 = max(line2)
            else:
                find-=1
        else:
            find -= 1

    result += 10 * find + find2

print(result)

print(time.time() - start_time)
