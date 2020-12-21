from math import prod
from collections import defaultdict
from itertools import permutations, product

with open("day20.txt") as f:
    tiles = f.read().split("\n\n")

tiles = {int(t[5:9]): t.splitlines()[1:] for t in tiles}


def sides(tile, include_reversed=True):
    if include_reversed:
        return {
            "N": tile[0],
            "S": tile[-1],
            "W": "".join([row[0] for row in tile]),
            "E": "".join([row[-1] for row in tile]),
            "RN": "".join(reversed(tile[0])),
            "RS": "".join(reversed(tile[-1])),
            "RW": "".join(reversed([row[0] for row in tile])),
            "RE": "".join(reversed([row[-1] for row in tile])),
        }
    else:
        return {
            "N": tile[0],
            "S": tile[-1],
            "W": "".join([row[0] for row in tile]),
            "E": "".join([row[-1] for row in tile]),
        }


def rotate(tdir, mdir, tile):
    if (tdir + mdir) in ("NS", "EW", "SN", "WE"):
        return tile
    elif tdir + mdir in ("NRN", "ERE", "SRS", "WRW"):
        return ["".join(reversed(row)) for row in reversed(tile)]
    elif tdir + mdir in ("NN", "ERW", "SS", "WRE"):
        return list(reversed(tile))
    elif tdir + mdir in ("NRS", "EE", "SRN", "WW"):
        return ["".join(reversed(row)) for row in tile]
    elif tdir + mdir in ("NRW", "ERS", "SRE", "WRN"):
        return ["".join(reversed(row)) for row in reversed(list(zip(*tile)))]
    elif tdir + mdir in ("NE", "EN", "SW", "WS"):
        return ["".join(row) for row in zip(*tile)]
    elif tdir + mdir in ("NW", "ERN", "SE", "WRS"):
        return ["".join(row) for row in reversed(list(zip(*tile)))]
    elif tdir + mdir in ("NRE", "ES", "SRW", "WN"):
        return ["".join(row) for row in zip(*tile[::-1])]
    else:
        raise Exception("Unknown rotation %s -> %s" % (tdir, mdir))


counts = defaultdict(int)
for (tid, tile), (mid, match) in permutations(tiles.items(), 2):
    if set(sides(tile).values()).intersection(set(sides(match).values())):
        counts[tid] += 1

print(prod(key for key, value in counts.items() if value == 2))

graph = {(0, 0): (1321, tiles[1321])}


def solve(coords):
    tsides = sides(graph[coords][1], include_reversed=False)
    for oid, other in tiles.items():
        if oid in [v[0] for v in graph.values()]:
            continue
        msides = sides(other)
        for (tdir, tedge), (mdir, medge) in product(tsides.items(), msides.items()):
            if tedge == medge:
                if tdir == "N":
                    mcoords = (coords[0] - 1, coords[1])
                elif tdir == "S":
                    mcoords = (coords[0] + 1, coords[1])
                elif tdir == "W":
                    mcoords = (coords[0], coords[1] - 1)
                elif tdir == "E":
                    mcoords = (coords[0], coords[1] + 1)
                else:
                    raise Exception(f"Unknown direction {tdir}")

                if mcoords not in graph:
                    graph[mcoords] = (oid, rotate(tdir, mdir, other))
                    solve(mcoords)


solve((0, 0))
minx = min(0, min(c[0] for c in graph.keys()))
miny = min(0, min(c[1] for c in graph.keys()))
grid = [
    [
        [row[1:-1] for row in graph[(row + minx, col + miny)][1][1:-1]]
        for col in range(12)
    ]
    for row in range(12)
]
joined = ["".join(row) for group in grid for row in zip(*group)]
serpent_offsets = [
    (-1, -1),
    (0, 0),
    (0, -1),
    (0, -2),
    (0, -7),
    (0, -8),
    (0, -13),
    (0, -14),
    (0, -19),
    (1, -3),
    (1, -6),
    (1, -9),
    (1, -12),
    (1, -15),
    (1, -18),
]
serpent_count = 0
for i, row in enumerate(joined):
    for j, item in enumerate(row):
        try:
            if {joined[i + o[1]][j + o[0]] for o in serpent_offsets} == {"#"}:
                serpent_count += 1
        except IndexError:
            continue
print("".join(joined).count("#") - 15 * serpent_count)
