from functools import reduce
from itertools import product
from operator import xor

word = 'hxtvlmkl'


def knot_hash(lengths, rounds=64, sparse_hash=False):
    nums = list(range(256))
    position = 0
    skip_size = 0

    for _ in range(rounds):
        for length in lengths:
            if length > len(nums):
                continue

            # Rotate the list so that we always reverse starting at 0, then
            # rotate it back.
            nums = nums[position:] + nums[:position]
            nums[:length] = reversed(nums[:length])
            nums = nums[-position:] + nums[:-position]

            position += length + skip_size
            position %= len(nums)
            skip_size += 1

    if sparse_hash:
        return nums

    dense_hash = [
        reduce(xor, nums[16 * i:16 * i + 16], 0)
        for i in range(16)
    ]

    return ''.join(hex(d)[2:].zfill(2) for d in dense_hash)


def get_binary(i):
    return bin(int('0x' + knot_hash(list(f"{word}-{i}".encode('utf-8')) + [17, 31, 73, 47, 23]), 16))[2:]


print(sum(get_binary(i).count('1') for i in range(128)))

# For part 2, iterate through each grid position and see if it's already
# been marked as part of a group. If it has, do nothing. Otherwise, start
# a recursive flood fill that marks every spot in the same group as this
# position. This seems like it would be O(2*n). We start numbering groups
# with `2`, since that's guaranteed higher than the binary values initially
# contained in the grid. We can then calculate the number of groups as
# `current_max - 1`.

grid = [
    list(map(int, get_binary(i).zfill(128)))
    for i in range(128)
]

current_max = 1

def fill(row, col, value=None):
    global current_max

    if not (0 <= row < 128 and 0 <= col < 128):
        return

    if grid[row][col] == 0:
        return

    if grid[row][col] == 1:
        if value is None:
            current_max += 1
            grid[row][col] = current_max
        else:
            grid[row][col] = value

        for a, b in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            fill(row + a, col + b, value=grid[row][col])


for row, col in product(range(128), range(128)):
    fill(row, col)

print(current_max - 1)
