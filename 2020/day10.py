from functools import reduce

with open("day10.txt") as f:
    adapters = list(sorted(int(line) for line in f.readlines()))

# Add the start and end joltages
adapters = [0] + adapters + [adapters[-1] + 3]

pairs = [abs(a - b) for a, b in zip(adapters, adapters[1:])]
print(pairs.count(1) * pairs.count(3))

sequenced = "".join(
    [str(sum([n - a <= 3 for n in adapters[i + 1 :]])) for i, a in enumerate(adapters)]
).split("1")


def reducer(total, num):
    if num == "332":
        return total * 7
    elif num == "32":
        return total * 4
    elif num == "2":
        return total * 2
    else:
        return total


print(reduce(reducer, sequenced, 1))
