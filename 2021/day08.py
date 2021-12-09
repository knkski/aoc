# Convert "words" to bitfields where 'a' is LSB and 'g' is MSB. For example,
# convert `ef` to `0b110000`. It's similar to doing `set('ef')`, but both more
# efficient, and easier to write code for with bitwise operators.
with open("day08.txt") as f:
    lines = [
        [
            [
                sum(1 << (ord(ch) - 97) for ch in word)
                for word in side.strip().split(" ")
            ]
            for side in line.strip().split("|")
        ]
        for line in f.readlines()
    ]

total = sum(bin(digit).count("1") in (2, 4, 3, 7) for _, digits in lines for digit in digits)

print(total)


def get(pats, length, filt=lambda _: True):
    return next(i for i in pats if bin(i).count("1") == length and filt(i))


total = 0
for patterns, digits in lines:
    solved = {
        1: get(patterns, 2),
        7: get(patterns, 3),
        4: get(patterns, 4),
        8: get(patterns, 7),
    }

    solved[3] = get(patterns, 5, lambda i: i & solved[1] == solved[1])
    solved[2] = get(patterns, 5, lambda i: i & solved[1] != solved[1] and bin(i & solved[4]).count("1") == 2)
    solved[5] = get(patterns, 5, lambda i: i & solved[1] != solved[1] and bin(i & solved[4]).count("1") == 3)
    solved[6] = get(patterns, 6, lambda i: i & solved[7] != solved[7])
    solved[9] = get(patterns, 6, lambda i: i & solved[4] == solved[4])
    solved[0] = get(patterns, 6, lambda i: i & solved[7] == solved[7] and i & solved[4] != solved[4])

    decoder = {v: k for k, v in solved.items()}
    total += int("".join(str(decoder[x]) for x in digits))

print(total)
