from collections import Counter, defaultdict

with open('day14.txt') as f:
    template, pairs = f.read().split('\n\n')
    pairs = dict(p.split(' -> ') for p in pairs.splitlines())
    template = Counter(''.join(p) for p in zip(template, template[1:]))


def grow(tmpl, n=10):
    for i in range(n):
        result = defaultdict(int)

        for pair, count in tmpl.items():
            insert = pairs[pair]

            result[pair[0] + insert] += count
            result[insert + pair[1]] += count

        tmpl = result

    totals = defaultdict(int)
    for pair, count in result.items():
        totals[pair[0]] += count
    totals[template[-1]] += 1
    return max(totals.values()) - min(totals.values())


print(grow(template.copy()))
print(grow(template.copy(), n=40))
