from math import prod

with open("day03.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def trees(x, y):
    return sum(
        lines[row][x * row // y % len(lines[0])] == "#"
        for row in range(y, len(lines), y)
    )


print(trees(3, 1))
print(prod(trees(*c) for c in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))
