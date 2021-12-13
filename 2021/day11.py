from itertools import product, count

with open("day11.txt") as f:
    grid = {
        (i, j): int(num)
        for i, row in enumerate(f.readlines())
        for j, num in enumerate(row.strip())
    }

offsets = [coord for coord in product(*(range(-1, 2) for _ in range(2))) if any(coord)]


def neighbor_coords(offs, coord):
    return [tuple(map(sum, zip(coord, offset))) for offset in offsets]


flashes = 0
for turns in count(1):
    for coord in grid:
        grid[coord] += 1

    flashed = set()
    while True:
        changed = False
        for coord in grid:
            if grid[coord] > 9:
                changed = True
                flashes += 1
                grid[coord] = 0
                flashed.add(coord)
                for neighbor in neighbor_coords(offsets, coord):
                    if neighbor in grid and neighbor not in flashed:
                        grid[neighbor] += 1
        if not changed:
            break

    if turns == 100:
        print(flashes)

    if set(grid.values()) == {0}:
        print(turns)
        break
