from operator import mul
from functools import reduce


def parse(line):
    op, coords = line.split(" ")
    coords = coords.split(",")
    coords = [list(map(int, c[2:].split(".."))) for c in coords]
    coords = [range(c[0], c[1] + 1) for c in coords]
    return op, coords


with open("day22.txt") as f:
    lines = [parse(line) for line in f.readlines()]


def overlap(recta, rectb):
    ranges = [range(max(a.start, b.start), min(a.stop, b.stop)) for a, b in zip(recta, rectb)]

    if not all(ranges):
        return None

    return ranges


def calc(bounds=None):
    rects = []

    for op, rect in lines:
        if bounds:
            rect = overlap(rect, bounds)
        if rect is None:
            continue

        # Handle intersections with existing rectangles
        overlaps = [(val, overlap(existing, rect)) for val, existing in rects]
        rects += [(-1 if val == 1 else 1, overlap) for val, overlap in overlaps if overlap]

        if op == "on":
            rects.append((1, rect))

    return sum(val * reduce(mul, map(len, r), 1) for val, r in rects)


print(calc((range(-50, 51), range(-50, 51), range(-50, 51))))
print(calc())
