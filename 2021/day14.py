from collections import Counter, defaultdict

with open('day14.txt') as f:
    template, pairs = f.read().split('\n\n')
    pairs = dict(p.split(' -> ') for p in pairs.splitlines())
    polymer = Counter(''.join(p) for p in zip(template, template[1:]))


def grow(poly, n=10):
    for i in range(n):
        result = defaultdict(int)

        for pair, count in poly.items():
            insert = pairs[pair]

            result[pair[0] + insert] += count
            result[insert + pair[1]] += count

        poly = result

    totals = defaultdict(int)
    for pair, count in result.items():
        totals[pair[0]] += count
    totals[template[-1]] += 1
    return max(totals.values()) - min(totals.values())


print(grow(polymer.copy()))
print(grow(polymer.copy(), n=40))
