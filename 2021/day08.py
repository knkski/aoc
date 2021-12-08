with open("day08.txt") as f:
    lines = [[item.strip().split(" ") for item in line.strip().split("|")] for line in f.readlines()]

total = sum(len(digit) in (2, 4, 3, 7) for _, digits in lines for digit in digits)

print(total)


def get(pats, length, filt=lambda _: True):
    return "".join(sorted(next(i for i in pats if len(i) == length and filt(i))))


total = 0
for patterns, digits in lines:
    solved = {
        1: get(patterns, 2),
        7: get(patterns, 3),
        4: get(patterns, 4),
        8: get(patterns, 7),
    }

    solved[3] = get(patterns, 5, lambda i: all(x in i for x in solved[1]))
    solved[5] = get(patterns, 5, lambda i: not all(x in i for x in solved[1]) and sum([x in i for x in solved[4]]) == 3)
    solved[2] = get(patterns, 5, lambda i: not all(x in i for x in solved[1]) and sum([x in i for x in solved[4]]) == 2)
    solved[0] = get(patterns, 6, lambda i: all(x in i for x in solved[7]) and not all(x in i for x in solved[4]))
    solved[6] = get(patterns, 6, lambda i: not all(x in i for x in solved[7]))
    solved[9] = get(patterns, 6, lambda i: all(x in i for x in solved[4]))

    decoder = {v: k for k, v in solved.items()}
    total += int("".join(str(decoder["".join(sorted(x))]) for x in digits))

print(total)
