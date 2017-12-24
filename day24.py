with open('day24.txt') as f:
    lines = f.readlines()


# We don't have to worry about reversing later on if we just also store a reversed copy
# right away. We then remove both the original and the copy in `without`.
parts = [tuple(map(int, l.split('/'))) for l in lines]
parts += [tuple(reversed(p)) for p in parts]


def without(lst, item):
    lst = lst[:]
    lst.remove(item)
    lst.remove(tuple(reversed(item)))
    return lst


def build(ports, root=None, i=100):
    if not ports:
        return

    if i == 0:
        return

    return {
        p: build(without(ports, p), p, i - 1)
        for p in ports
        if (not root and p[0] == 0) or (root and root[1] == p[0])
    }


def find_max(tree):
    if not tree:
        return 0

    return max(sum(item) + find_max(st) for item, st in tree.items())


def add(strength, max_longest):
    depth, strength_sum = max_longest
    return depth, strength + strength_sum


def find_max_longest(tree, depth=0):
    if not tree:
        return depth, 0

    return max(
        add(sum(item), find_max_longest(st, depth + 1))
        for item, st in tree.items()
    )


bridges = build(parts)
print(find_max(bridges))
print(find_max_longest(bridges)[1])
