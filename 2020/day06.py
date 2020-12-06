with open("day06.txt") as f:
    groups = [
        [set(response) for response in group.splitlines()]
        for group in f.read().split("\n\n")
    ]

print(sum(len(set.union(*group)) for group in groups))
print(sum(len(set.intersection(*group)) for group in groups))
