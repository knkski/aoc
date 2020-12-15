from functools import reduce

with open("day15.txt") as f:
    spoken = list(map(int, f.read().strip().split(",")))

seen = {num: i for i, num in enumerate(spoken)}


def reducer(memo, i):
    seen, last = memo
    if last not in seen:
        seen[last] = i
        last = 0
    else:
        seen[last], last = i, i - seen[last]
    return seen, last


for steps in (2020, 30000000):
    _, last = reduce(
        reducer,
        range(len(spoken), steps - 1),
        (seen.copy(), 0),
    )
    print(last)
