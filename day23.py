from collections import defaultdict
from itertools import count

with open('day23.txt') as f:
    instructions = [l.strip().split(' ') for l in f.readlines()]


registers = defaultdict(int)

current = 0
total = 0

for i in count():
    try:
        instruction, register, value = instructions[current]
    except IndexError:
        break

    def get(val):
        try:
            return int(val)
        except ValueError:
            return registers[val]

    if instruction == 'set':
        registers[register] = get(value)
    elif instruction == 'sub':
        registers[register] -= get(value)
    elif instruction == 'mul':
        total += 1
        registers[register] *= get(value)
    elif instruction == 'jnz':
        if get(register) != 0:
            current += int(value)
            continue

    current += 1

print(total)


def isprime(n):
    """Returns True if n is prime."""

    if n in [2, 3]:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


print(len([n for n in range(108400, 125401, 17) if not isprime(n)]))
