import numpy as np
from functools import reduce

with open('day21.txt') as f:
    rules_string = f.readlines()


def chunked(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def to_arr(s):
    size = len(s.split('/')[0])
    return np.array(list(s.replace('/', '')), dtype=str).reshape(size, size)


def to_str(arr):
    return '/'.join(''.join(map(str, row)) for row in arr)


def generate_rules(memo, rule_string):
    pred, succ = rule_string.strip().split(' => ')

    np_rule = to_arr(pred)

    for i in range(4):
        memo[to_str(np.rot90(np_rule, i))] = succ

    np_rule = np.fliplr(np_rule)

    for i in range(4):
        memo[to_str(np.rot90(np_rule, i))] = succ

    return memo


rules = reduce(generate_rules, rules_string, {})

start = to_arr('.#./..#/###')


def generate(art, rounds):
    for _ in range(rounds):
        size = art.shape[0]

        divisor = 2 if size % 2 == 0 else 3

        def get_new_chunk(chunk):
            return to_arr(rules[to_str(chunk)])

        chunks = [
            get_new_chunk(art[divisor*i:divisor*i+divisor, divisor*j:divisor*j+divisor])
            for i in range(size // divisor)
            for j in range(size // divisor)
        ]

        art = np.block(list(chunked(chunks, size // divisor)))

    return art


print(np.unique(generate(start, rounds=5), return_counts=True)[1][0])
print(np.unique(generate(start, rounds=18), return_counts=True)[1][0])
