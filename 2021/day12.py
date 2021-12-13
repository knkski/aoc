from collections import defaultdict

with open("day12.txt") as f:
    lines = [line.strip() for line in f.readlines()]

graph = defaultdict(set)

for line in lines:
    a, b = line.split("-")

    if a != "end" and b != "start":
        graph[a].add(b)

    if b != "end" and a != "start":
        graph[b].add(a)


def no_backsies(path):
    current = path[-1]
    if current == "end":
        return 1

    return sum(
        no_backsies(path + [nxt]) for nxt in graph[current] if nxt.isupper() or nxt not in path
    )


print(no_backsies(["start"]))


def ok_a_little_backsies(path, little=None):
    current = path[-1]
    if current == "end":
        return 1

    return sum(
        ok_a_little_backsies(
            path + [nxt],
            little=nxt if little is None and nxt.islower() and nxt in path else little,
        )
        for nxt in graph[current]
        if nxt.isupper() or (nxt.islower() and little is None or nxt not in path)
    )


print(ok_a_little_backsies(["start"]))
