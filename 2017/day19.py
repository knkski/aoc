from string import ascii_uppercase
from enum import Enum

with open('day19.txt') as f:
    lines = f.readlines()


Direction = Enum('Direction', 'UP DOWN LEFT RIGHT')

position = [0, lines[0].index('|')]

direction = Direction.DOWN
encountered = []
steps = 0

while True:
    char = lines[position[0]][position[1]]

    # For all of these characters, just keep going
    if char in '|-' + ascii_uppercase:
        if char in ascii_uppercase:
            encountered.append(char)

        if direction == Direction.DOWN:
            position[0] += 1
        elif direction == Direction.UP:
            position[0] -= 1
        elif direction == Direction.LEFT:
            position[1] -= 1
        elif direction == Direction.RIGHT:
            position[1] += 1

    # Turn here
    elif char == '+':
        if direction in [Direction.DOWN, Direction.UP]:
            if lines[position[0]][position[1] + 1] != ' ':
                direction = Direction.RIGHT
                position[1] += 1
            else:
                direction = Direction.LEFT
                position[1] -= 1
        elif direction in [Direction.LEFT, Direction.RIGHT]:
            if position[0] < len(lines) - 1 and lines[position[0] + 1][position[1]] != ' ':
                direction = Direction.DOWN
                position[0] += 1
            else:
                direction = Direction.UP
                position[0] -= 1

    # We've reached the end of the line
    else:
        break

    steps += 1


print(''.join(encountered))
print(steps)
