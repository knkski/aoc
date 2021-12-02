from collections import deque
from itertools import islice


def sliding_window(it, n):
    """https://docs.python.org/3/library/itertools.html#itertools-recipes"""

    it = iter(it)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def count_increases(it, window=1):
    grouped = sliding_window(it, window)
    return sum(sum(x[1]) > sum(x[0]) for x in sliding_window(grouped, 2))


with open("day01.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

print(count_increases(lines))
print(count_increases(lines, window=3))
