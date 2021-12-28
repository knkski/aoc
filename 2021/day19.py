from itertools import product, combinations
from math import copysign

with open("day19.txt") as f:
    scanners = {
        group.strip().splitlines()[0]: tuple(
            tuple(map(int, line.split(","))) for line in group.strip().splitlines()[1:]
        )
        for group in f.read().split("\n\n")
    }

rotations = [
    (1, 2, 3),
    (-1, -2, 3),
    (-1, -3, -2),
    (-1, 2, -3),
    (-1, 3, 2),
    (-2, -1, -3),
    (-2, -3, 1),
    (-2, 1, 3),
    (-2, 3, -1),
    (-3, -1, 2),
    (-3, -2, -1),
    (-3, 1, -2),
    (-3, 2, 1),
    (1, -2, -3),
    (1, -3, 2),
    (1, 3, -2),
    (2, -1, 3),
    (2, -3, -1),
    (2, 1, -3),
    (2, 3, 1),
    (3, -1, -2),
    (3, -2, 1),
    (3, 1, 2),
    (3, 2, -1),
]


def rotate(block, rot):
    return [
        (
            copysign(1, rot[0]) * row[abs(rot[0]) - 1],
            copysign(1, rot[1]) * row[abs(rot[1]) - 1],
            copysign(1, rot[2]) * row[abs(rot[2]) - 1],
        )
        for row in block
    ]


def is_match(existing, sb):
    for rotation in rotations:
        rotated = rotate(sb, rotation)
        offsets = {
            tuple(a - b for a, b in zip(beacona, beaconb))
            for beacona, beaconb in product(existing, rotated)
        }
        for a, b, c in offsets:
            adjusted = []
            matches = 0
            for x, y, z in rotated:
                adj = x + a, y + b, z + c
                adjusted.append(adj)
                if adj in existing:
                    matches += 1

            if matches >= 12:
                return adjusted, (a, b, c)
    return None, None


def align():
    first = list(scanners.items())[0]
    del scanners[first[0]]
    survey = {tuple(beacon) for beacon in first[1]}
    positions = [(0, 0, 0)]

    while scanners:
        for name, scanner in scanners.items():
            adjusted, position = is_match(survey, scanner)
            if adjusted is not None:
                positions.append(tuple(position))
                survey.update(adjusted)
                break
        del scanners[name]

    count = len(survey)
    furthest = max(
        abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        for a, b in combinations(positions, 2)
    )

    return count, furthest


count, furthest = align()
print(count)
print(furthest)
