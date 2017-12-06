from itertools import count

blocks = '0 5 10 0 11 14 13 4 11 8 8 7 1 4 12 11'
blocks = list(map(int, blocks.split(' ')))

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
