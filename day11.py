from operator import add
from functools import reduce

with open('day11.txt') as f:
    steps = f.read().strip().split(',')


def step(memo, direction):
    if direction == 'n':
        movement = 0, 1, -1
    elif direction == 'ne':
        movement = 1, 0, -1
    elif direction == 'se':
        movement = 1, -1, 0
    elif direction == 's':
        movement = 0, -1, 1
    elif direction == 'sw':
        movement = -1, 0, 1
    elif direction == 'nw':
        movement = -1, 1, 0
    else:
        raise Exception(f"Bad step `{memo[0]}`")

    current = tuple(map(add, memo[0], movement))
    farthest = max(memo[1], max(map(abs, current)))

    return current, farthest

current, farthest = reduce(step, steps, ((0, 0, 0), 0))

print(max(map(abs, current)))
print(farthest)
