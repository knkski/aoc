with open('day22.txt') as f:
    # 1/0 is easier to work with below than #/. Center grid around 0, 0
    starting_grid = {
        (-12 + i, -12 + j): 1 if item == '#' else 0
        for i, row in enumerate(f.readlines())
        for j, item in enumerate(row)
    }

# Directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Node state
CLEAN = 0
INFECTED = 1
WEAKENED = 2
FLAGGED = 3


def infect(grid, bursts=10000, smart=False):
    position = 0, 0
    direction = 0

    total = 0

    for _ in range(bursts):
        node = grid.get(position, 0)

        if node == 0:
            direction -= 1
            grid[position] = WEAKENED if smart else INFECTED

            if not smart:
                total += 1

        elif node == 1:
            direction += 1
            grid[position] = FLAGGED if smart else CLEAN

        elif node == 2:
            grid[position] = INFECTED

            if node != INFECTED:
                total += 1

        elif node == 3:
            direction += 2
            grid[position] = CLEAN

        else:
            raise Exception(f'Invalid node state `{node}`')

        direction %= 4

        if direction == UP:
            position = position[0] - 1, position[1]
        elif direction == RIGHT:
            position = position[0], position[1] + 1
        elif direction == DOWN:
            position = position[0] + 1, position[1]
        elif direction == LEFT:
            position = position[0], position[1] - 1
        else:
            raise Exception(f'Invalid direction `{direction}`')

    return total


print(infect(starting_grid.copy()))
print(infect(starting_grid.copy(), bursts=10000000, smart=True))
