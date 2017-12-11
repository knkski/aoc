from itertools import count


with open('day5.txt') as f:
    offsets = [int(offset) for offset in f.readlines()]


def calculate_jumps(offsets, incrementer):
    current = 0

    for i in count():
        try:
            jump = offsets[current]
            offsets[current] += incrementer(jump)
            current += jump
        except IndexError:
            return i

print(calculate_jumps(offsets[:], lambda j: 1))
print(calculate_jumps(offsets[:], lambda j: -1 if j >= 3 else 1))
