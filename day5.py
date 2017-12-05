from itertools import count

def calculate_jumps(incrementer):
    with open('day5_input.txt') as f:
        offsets = [int(offset) for offset in f.readlines()]

    current = 0

    for i in count():
        try:
            jump = offsets[current]
            offsets[current] += incrementer(jump)
            current += jump
        except IndexError:
            print(i)
            break

calculate_jumps(lambda j: 1)
calculate_jumps(lambda j: -1 if j >= 3 else 1)
