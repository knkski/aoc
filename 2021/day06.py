from collections import Counter

with open("day06.txt") as f:
    counts = Counter(map(int, f.read().strip().split(',')))

for i in range(256):
    if i == 80:
        print(sum(counts.values()))

    counts = {
        0: counts[1],
        1: counts[2],
        2: counts[3],
        3: counts[4],
        4: counts[5],
        5: counts[6],
        6: counts[7] + counts[0],
        7: counts[8],
        8: counts[0],
    }

print(sum(counts.values()))
