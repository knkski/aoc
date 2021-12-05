from collections import defaultdict

with open("day05.txt") as f:
    lines = [[f.split(",") for f in line.strip().split(" -> ")] for line in f.readlines()]

# Store both grids in one. First item is horizontal/vertical only grid, second
# item is diagonal-inclusive grid.
grid = defaultdict(lambda: [0, 0])


def rng(a, b):
    """Returns inclusive range from a to b, stepping backwards if necessary."""
    if a < b:
        return range(a, b + 1)
    else:
        return range(a, b - 1, -1)


for line in lines:
    ((x1, y1), (x2, y2)) = line
    x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])

    if x1 == x2:
        for y in rng(y1, y2):
            grid[(x1, y)][0] += 1
            grid[(x1, y)][1] += 1
    elif y1 == y2:
        for x in rng(x1, x2):
            grid[(x, y1)][0] += 1
            grid[(x, y1)][1] += 1
    else:
        for coord in zip(rng(x1, x2), rng(y1, y2)):
            grid[coord][1] += 1

print(sum(v[0] > 1 for v in grid.values()))
print(sum(v[1] > 1 for v in grid.values()))
