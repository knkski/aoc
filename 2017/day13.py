from itertools import count
import re

with open('day13.txt') as f:
    layers = f.readlines()

layers = dict(map(int, re.findall('\w+', l)) for l in layers)

def is_caught(layer, depth, delay):
    return ((layer + delay) % (2 * depth - 2)) == 0

print(sum(
    layer * depth
    for layer, depth in layers.items()
    if is_caught(layer, depth, 0)
))

print(next(
    delay
    for delay in count()
    if not any(
        is_caught(layer, depth, delay)
        for layer, depth in layers.items()
    )
))
