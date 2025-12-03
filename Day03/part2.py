import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def rec(line, parts, needed=12):
    if len(parts) == needed:
        return True

    if len(line) < needed - len(parts):
        return False

    for find in reversed(range(10)):
        if str(find) in line:
            i = line.index(str(find))
            parts.append(str(find))
            test = rec(line[i + 1:], parts, needed)
            if test:
                return test
            del parts[-1]
        find -= 1

    return False


som = 0
for line in lines:
    result = []
    parts = rec(line, result)
    som += int(''.join(result))

print(som)

print(time.time() - start_time)
