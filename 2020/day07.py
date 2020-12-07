from collections import defaultdict

with open("day07.txt") as f:
    lines = f.readlines()

bags = defaultdict(list)
for line in lines:
    outer, inners = line.strip("\n.").split(" contain ")
    if inners != "no other bags":
        for inner in inners.split(", "):
            bags[" ".join(outer.split(" ")[:-1])] += [
                (int(inner.split(" ")[0]), " ".join(inner.split(" ")[1:-1]))
            ]


def holders(colors):
    hs = {
        outer
        for outer, inner in bags.items()
        for color in colors
        if color in [i[1] for i in inner] and outer not in colors
    }
    return colors.union(*[holders({h}) for h in hs])


# -1 because shiny gold doesn't hold itself
print(len(holders({"shiny gold"})) - 1)


def holdees(color):
    return sum(b[0] for b in bags[color]) + sum(
        b[0] * holdees(b[1]) for b in bags[color]
    )


print(holdees("shiny gold"))
