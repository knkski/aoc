from functools import reduce
from operator import mul

with open("day09.txt") as f:
    lines = [[int(f) for f in line.strip()] for line in f.readlines()]

grid = {(i, j): num for i, row in enumerate(lines) for j, num in enumerate(row)}
total = 0

for i, row in enumerate(lines):
    for j, item in enumerate(row):
        offsets = ((1, 0), (-1, 0), (0, 1), (0, -1))
        neighbors = [(i + o[0], j + o[1]) for o in offsets]
        if any(grid.get(n) is not None and grid.get(n) <= item for n in neighbors):
            continue

        total += item + 1

print(total)


def find_basin(coords, found):
    if coords in found:
        return found

    if coords[0] < 0 or coords[1] < 0 or coords[0] >= len(lines) or coords[1] >= len(lines[0]):
        return found

    if lines[coords[0]][coords[1]] == 9:
        return found

    found.add(coords)

    neighbors = {
        (coords[0] + 1, coords[1]),
        (coords[0] - 1, coords[1]),
        (coords[0], coords[1] + 1),
        (coords[0], coords[1] - 1),
    }

    return set.union(*[find_basin(c, found) for c in neighbors])


seen = set()
basin_sizes = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if (i, j) in seen:
            continue

        basin = find_basin((i, j), set())
        seen |= basin
        basin_sizes.append(len(basin))

print(reduce(mul, list(sorted(basin_sizes))[-3:], 1))
