from operator import add, mul

from parsita import TextParsers, lit, reg, rep
from parsita.util import constant


def reduce(args):
    result, factors = args
    for op, factor in factors:
        result = op(result, factor)
    return result


class Homework(TextParsers):
    number = reg(r"\d+") > int
    plus = lit("+") > constant(add)
    times = lit("*") > constant(mul)
    operator = plus | times

    # No precedence
    base = "(" >> unprecedented << ")" | number
    unprecedented = base & rep(operator & base) > reduce

    # Addition first, then multiplication
    base = "(" >> multiplication << ")" | number
    addition = base & rep(plus & base) > reduce
    multiplication = addition & rep(times & addition) > reduce


with open("day18.txt") as f:
    problems = f.readlines()

print(sum(Homework.unprecedented.parse(p).value for p in problems))
print(sum(Homework.multiplication.parse(p).value for p in problems))
