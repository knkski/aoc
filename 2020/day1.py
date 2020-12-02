import itertools
import math

with open("day1.txt") as f:
    nums = [int(line) for line in f.readlines()]

for entry_count in (2, 3):
    for entries in itertools.combinations(nums, entry_count):
        if sum(entries) == 2020:
            print(math.prod(entries))
