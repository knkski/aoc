with open("day13.txt") as f:
    paper, folds = f.read().split("\n\n")
    paper = {tuple(map(int, line.strip().split(","))) for line in paper.splitlines()}
    folds = [f[11:].split("=") for f in folds.splitlines()]

for i, (direction, fold) in enumerate(folds):
    fold = int(fold)
    xmax = max(x for x, y in paper) + 1
    ymax = max(y for x, y in paper) + 1

    paper = {
        (
            x - 2 * abs(x - fold) if direction == "x" and x > fold else x,
            y - 2 * abs(y - fold) if direction == "y" and y > fold else y,
        )
        for x, y in paper
    }

    if i == 0:
        print(len(paper))

ymax = max(y for x, y in paper) + 1
for i in range(ymax):
    print("".join("#" if (j, i) in paper else " " for j in range(xmax)))
