from itertools import islice


def gen(start, factor, filter=None):
    num = start

    while True:
        num = num * factor % 2147483647

        if filter is None or filter(num):
            yield num & 0xFFFF


gen_a_1 = gen(277, 16807)
gen_b_1 = gen(349, 48271)
gen_a_2 = gen(277, 16807, lambda n: n % 4 == 0)
gen_b_2 = gen(349, 48271, lambda n: n % 8 == 0)


print(sum(a == b for a, b in islice(zip(gen_a_1, gen_b_1), 40000000)))
print(sum(a == b for a, b in islice(zip(gen_a_2, gen_b_2),  5000000)))
