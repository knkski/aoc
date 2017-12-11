from itertools import count

with open('day6.txt') as f:
    blocks = list(map(int, f.read().split(' ')))

memory = []

for i in count():
    if blocks in memory:
        print(i)
        print(i - memory.index(blocks))
        break

    memory.append(blocks[:])

    max_val = max(blocks)
    highest = blocks.index(max_val)

    blocks[highest] = 0

    for _ in range(max_val):
        highest += 1
        highest %= len(blocks)
        blocks[highest] += 1
