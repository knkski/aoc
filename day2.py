from functools import reduce
from itertools import product

with open('day2.txt') as f:
    numbers = [list(map(int, n.split('\t'))) for n in f.read().strip().split('\n')]

checksum = sum([max(row) - min(row) for row in numbers])

print(checksum)

def reducer(memo, row):
    for i, j in product(row, row):
        if i != j and i / j == i // j:
            return memo + i // j

print(reduce(reducer, numbers, 0))
