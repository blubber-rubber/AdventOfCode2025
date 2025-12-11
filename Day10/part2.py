import math
import time
import re
from collections import defaultdict
import pulp

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def get_solution_ranges(inequalities):
    ineqs = defaultdict(list)

    for ineq in inequalities:
        free_symbols = list(ineq.free_symbols)
        if len(free_symbols) == 1:
            ineqs[free_symbols[0]].append(ineq)

    solution_range = {}
    for s, s_ineqs in ineqs.items():
        ineq = solve(s_ineqs)
        if ineq == False:
            lower = 0
            upper = -1
        elif isinstance(ineq, Eq):
            lower = math.ceil(ineq.rhs)
            upper = math.floor(ineq.rhs)
        else:
            lower = math.ceil(ineq.args[0].lhs)
            upper = math.floor(ineq.args[1].rhs)

        solution_range[s] = (lower, upper)

    return solution_range


def get_distance(goal, buttons):
    prob = pulp.LpProblem("MinimizeSum", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{i}", cat='Integer', lowBound=0, upBound=min(g for i, g in enumerate(goal) if i in b)) for
         i, b in
         enumerate(buttons)]

    prob += pulp.lpSum(x)

    n_lights = len(goal)
    for i in range(n_lights):
        prob += sum(x[j] for j, b in enumerate(buttons) if i in b) == goal[i]

    prob.solve()

    print("Status:", pulp.LpStatus[prob.status])
    print("Optimal value:", pulp.value(prob.objective))
    print("Optimal solution:", [v.varValue for v in x])

    return round(pulp.value(prob.objective))


def recursive(inequalities, variables, d):
    if all(ineq == True for ineq in inequalities):
        return sum(d.values()).subs(variables) + sum(variables.values())
    ranges = get_solution_ranges(inequalities)

    var, rang = min([(k, v) for k, v in ranges.items()], key=lambda x: x[1][1] - x[1][0])
    lower, upper = rang
    possible = []

    for v in range(lower, upper + 1):
        variables[var] = v
        new_ineqs = [ineq.subs(variables) for ineq in inequalities]
        if not any(i == False for i in new_ineqs):
            possible.append(recursive(new_ineqs, variables, d))
        del variables[var]

    if not possible:
        return math.inf
    return min(possible)


total = 0
for i, line in enumerate(lines):
    goal, buttons, joltages = re.match('^\[(.*)] (.*) \{(.*)}$', line).groups()

    goal = tuple(1 if x == '#' else 0 for x in goal)
    buttons = [tuple(int(x) for x in g.groups()[0].split(',')) for g in re.finditer('\(([^)]*)\)', buttons)]

    buttons.sort(key=lambda x: -len(x))
    joltages = tuple(int(x) for x in joltages.split(','))

    total += get_distance(joltages, buttons)
    print(i + 1, 'done')

print(total)
print(time.time() - start_time)
