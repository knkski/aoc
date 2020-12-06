from itertools import groupby

with open("day05.txt") as f:
    data = sorted(
        [
            (int(line[:7].replace("F", "0").replace("B", "1"), 2) << 3)
            + int(line[7:].replace("L", "0").replace("R", "1"), 2)
            for line in f.readlines()
        ]
    )

print(data[-1])

# Skip first and last rows, then print all seats in all rows where
# the seat exists in expected, but not assigned.
rows = [list(g) for _, g in groupby(data, lambda x: x >> 3)][1:-1]
for row in rows:
    expected = set(range(row[0], row[0] + 8))
    if (diff := expected.difference(set(row))) :
        print(diff)
