with open("day01.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

print(sum(a < b for a, b in zip(lines, lines[1:])))
print(sum(a < b for a, b in zip(lines, lines[3:])))
