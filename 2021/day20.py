from itertools import product, cycle

with open("day20.txt") as f:
    algo, grid = [line.strip() for line in f.read().split("\n\n")]

    algo = ["1" if a == "#" else "0" for a in algo]
    grid = {
        (i, j): "1" if item == "#" else "0"
        for i, row in enumerate(grid.splitlines())
        for j, item in enumerate(row.strip())
    }

OFFSETS = [coord for coord in product(range(-1, 2), range(-1, 2))]


def replace(g, default):
    new = {}

    topleft = min(g)
    bottomright = max(g)

    rows = range(topleft[0] - 1, bottomright[0] + 2)
    cols = range(topleft[1] - 1, bottomright[1] + 2)

    return {
        (i, j): algo[
            int(
                "".join(
                    g.get(n, default) for n in [(i + o[0], j + o[1]) for o in OFFSETS]
                ),
                2,
            )
        ]
        for i in rows
        for j in cols
    }


new = grid
for i, default in zip(range(50), cycle("01")):
    new = replace(new, default)

    if i in (1, 49):
        print(list(new.values()).count("1"))
