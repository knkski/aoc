from itertools import product

with open("day17.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def neighbor_coords(grid, offsets, coord):
    return [tuple(map(sum, zip(coord, offset))) for offset in offsets]


def neighbor_vals(grid, offsets, coord):
    return [grid.get(tuple(map(sum, zip(coord, offset))), ".") for offset in offsets]


def run(dims=3):
    grid = {}
    offsets = [
        coord for coord in product(*(range(-1, 2) for _ in range(dims))) if any(coord)
    ]
    for x, row in enumerate(lines):
        for y, value in enumerate(row):
            grid[(x, y) + (0,) * (dims - 2)] = value

    for _ in range(6):
        to_check = list(grid.keys()) + [
            neighbor
            for element in grid
            for neighbor in neighbor_coords(grid, offsets, element)
        ]
        new_grid = grid.copy()
        for coord in to_check:
            ns = neighbor_vals(grid, offsets, coord)
            if grid.get(coord, ".") == "#":
                if ns.count("#") in (2, 3):
                    new_grid[coord] = "#"
                else:
                    new_grid[coord] = "."
            else:
                if ns.count("#") == 3:
                    new_grid[coord] = "#"
        grid = new_grid

    return list(grid.values()).count("#")


print(run())
print(run(dims=4))
