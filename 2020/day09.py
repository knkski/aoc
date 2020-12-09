from itertools import combinations

with open("day09.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]


for i in range(25, len(lines)):
    for a, b in combinations(lines[i - 25 : i], 2):
        if a + b == lines[i]:
            break
    else:
        weakness = lines[i]
        break

print(weakness)

for i in range(len(lines)):
    for j in range(i, len(lines)):
        span = lines[i:j]
        if len(span) > 1 and sum(span) == weakness:
            print(min(span) + max(span))
