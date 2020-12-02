import re

pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


with open("day02.txt") as f:
    data = [pattern.match(line).groups() for line in f.readlines()]

totals = [0, 0]

for min, max, letter, string in data:
    min, max = int(min), int(max)
    if min <= string.count(letter) <= max:
        totals[0] += 1

    chars = string[min - 1] + string[max - 1]
    if chars.count(letter) == 1:
        totals[1] += 1

print("\n".join(map(str, totals)))
