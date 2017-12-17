from string import ascii_lowercase
import re

with open('day16.txt') as f:
    moves = f.read().split(',')


def dance(rounds=1):
    programs = list(ascii_lowercase[:16])

    for i in range(rounds):
        for move in moves:
            if move[0] == 'x':
                a, b = map(int, re.findall(r'\d+', move))

                programs[a], programs[b] = programs[b], programs[a]

            elif move[0] == 's':
                size = int(move[1:])

                programs = programs[-size:] + programs[:-size]

            elif move[0] == 'p':
                index_a = programs.index(move[1])
                index_b = programs.index(move[3])

                programs[index_a], programs[index_b] = programs[index_b], programs[index_a]
            else:
                raise Exception('Invalid dance move.')

    return ''.join(programs)


# Dance once, and then dance just enough so that it loops back around
# to the same place it would be at for 1 billion rounds. The dance
# repeats itself at 24 rounds, and 1000000000 % 24 == 40 % 24 == 16
print(dance())
print(dance(rounds=40))
