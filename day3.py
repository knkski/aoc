from itertools import islice, count

number = 347991


def spiral_coords():
    '''Yields coordinates in a spiral pattern.'''
    x, y = 0, 0
    direction = 0

    yield 0, 0

    for i in count(1):
        for _ in range(2):
            for j in range(i):
                if direction == 0:
                    x += 1
                elif direction == 1:
                    y += 1
                elif direction == 2:
                    x -= 1
                elif direction == 3:
                    y -= 1
                else:
                    raise Exception("Something went horribly wrong!")

                yield x, y

            direction += 1
            direction %= 4

# Calculate the spiral coordinates of our number, then sum the difference
# from (0, 0). Subtract one first since we want to slice up to but not
# including the number we want.
coords = spiral_coords()
num_coords = next(islice(coords, number - 1, None))
print(sum(abs(c) for c in num_coords))


# Iteratively calculate each sum. Assumes the answer can be found in a
# 11x11 grid, which turns out to be the case
coords = spiral_coords()

grid = [[0] * 11 for row in range(11)]

x = 5
y = 5

grid[y][x] = 1

for coords in spiral_coords():
    current_x, current_y = x + coords[0], y - coords[1]

    total = \
        grid[current_y - 1][current_x - 1] + \
        grid[current_y - 1][current_x    ] + \
        grid[current_y - 1][current_x + 1] + \
        grid[current_y    ][current_x - 1] + \
        grid[current_y    ][current_x    ] + \
        grid[current_y    ][current_x + 1] + \
        grid[current_y + 1][current_x - 1] + \
        grid[current_y + 1][current_x    ] + \
        grid[current_y + 1][current_x + 1]

    grid[current_y][current_x] = total

    if total > number:
        print(total)
        break
