import re

with open('day12.txt') as f:
    lines = f.readlines()

def transform(line):
    key, *vals = re.findall('\d+', line)
    return key, vals

nodes = dict(map(transform, lines))
groups = {}

def find_connected(root, node):
    if node in groups[root]:
        return

    groups[root].append(node)

    for neighbor in nodes[node]:
        find_connected(root, neighbor)

for node in nodes.keys():
    already_seen = [item for items in groups.values() for item in items]

    if node not in already_seen:
        groups[node] = []
        find_connected(node, node)

print(len(groups['0']))
print(len(groups))
