from itertools import count

with open("day25.txt") as f:
    start = {
        (i, j): item for i, line in enumerate(f.readlines()) for j, item in enumerate(line.rstrip())
    }


def step(grid):
    width = max(g[1] for g in grid)
    height = max(g[0] for g in grid)

    horizontal = grid.copy()

    for i, j in grid:
        if grid[(i, j)] == ">":
            to = (i, (j + 1) % (width + 1))
            if grid[to] == ".":
                horizontal[(i, j)], horizontal[to] = grid[to], grid[(i, j)]

    vertical = horizontal.copy()
    for i, j in horizontal:
        if horizontal[(i, j)] == "v":
            to = ((i + 1) % (height + 1), j)
            if horizontal[to] == ".":
                vertical[(i, j)], vertical[to] = horizontal[to], horizontal[(i, j)]

    return vertical


stepped = start
for i in count(1):
    old = stepped
    stepped = step(stepped)
    if old == stepped:
        print(i)
        break
