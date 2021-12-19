from math import floor, ceil
from dataclasses import dataclass
from itertools import permutations


@dataclass
class Node:
    """Node."""

    left: "Node"
    right: "Node"

    def __str__(self):
        """Do."""
        return f"[{self.left}, {self.right}]"

    def __add__(self, other):
        """Do."""
        return Node(self, other)


def convert(asdf):
    """Convert."""
    if isinstance(asdf, int):
        return asdf

    return Node(convert(asdf[0]), convert(asdf[1]))


def flatten(tree):
    flattened = []
    for ch in str(tree):
        if ch in "[],":
            if flattened and flattened[-1].isdigit():
                flattened[-1] = int(flattened[-1])
            flattened.append(ch)
        elif ch.isdigit() and flattened[-1].isdigit():
            flattened[-1] += ch
        elif ch.isdigit():
            flattened.append(ch)
        elif ch == " ":
            pass
        else:
            raise ValueError(ch)
    return flattened


def explode(tree):
    parsed = flatten(tree)
    depth = 0
    for i in range(len(parsed)):
        if parsed[i] == "[":
            depth += 1
        if parsed[i] == "]":
            depth -= 1
        if depth > 4 and parsed[i] == "[" and parsed[i + 4] == "]":
            break
    else:
        return tree, False

    left = parsed[i + 1]
    right = parsed[i + 3]
    for j in range(i, 0, -1):
        if isinstance(parsed[j], int):
            parsed[j] += left
            break
    for j in range(i + 5, len(parsed)):
        if isinstance(parsed[j], int):
            parsed[j] += right
            break

    parsed = "".join(map(str, parsed[:i] + ["0"] + parsed[i + 5:]))
    return convert(eval(parsed)), True


def split(tree) -> bool:
    parsed = flatten(tree)

    for i in range(len(parsed)):
        if isinstance(parsed[i], int) and parsed[i] > 9:
            break
    else:
        return tree, False

    left = floor(parsed[i] / 2)
    right = ceil(parsed[i] / 2)
    parsed = parsed[:i] + ["[", left, ",", right, "]"] + parsed[i + 1:]
    parsed = "".join(map(str, parsed))

    return convert(eval(parsed)), True


def reduce(tree):
    changed = True
    while changed:
        tree, changed = explode(tree)
        if changed:
            continue

        tree, changed = split(tree)

    return tree


def mag(tree):
    if isinstance(tree, int):
        return tree
    return 3 * mag(tree.left) + 2 * mag(tree.right)


with open("day18.txt") as f:
    converted = [convert(eval(line.strip())) for line in f.readlines()]

summed = converted[0]
for item in converted[1:]:
    summed = reduce(summed + item)

print(mag(summed))

max_mag = max(mag(reduce(left + right)) for left, right in permutations(converted, 2))
print(max_mag)
