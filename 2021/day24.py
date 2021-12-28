from itertools import combinations_with_replacement

with open("day24.txt") as f:
    ops = [line.strip().split(" ") for line in f.readlines()]


TABLE = """
0123456789ABCD

[0] - 2 == [D]
[1] - 3 == [C]
[2] + 1 == [B]
[3] - 6 == [4]
[5] - 8 == [A]
[6] + 0 == [7]
[8] - 7 == [9]
"""


def get(state, reg_or_val):
    try:
        return int(reg_or_val)
    except ValueError:
        return state[reg_or_val]


def validate(lines, model_number):
    state = {"w": 0, "x": 0, "y": 0, "z": 0}

    model_number = iter(model_number)

    for op, reg, *val in lines:
        if val:
            val = val[0]
        if op == "inp":
            foo = int(next(model_number))
            state[reg] = foo
        elif op == "add":
            state[reg] += get(state, val)
        elif op == "mul":
            state[reg] *= get(state, val)
        elif op == "div":
            state[reg] //= get(state, val)
        elif op == "mod":
            state[reg] %= get(state, val)
        elif op == "eql":
            state[reg] = int(state[reg] == get(state, val))
        else:
            0 / 0

    return state["z"] == 0


highest = "99893999291967"
lowest = "34171911181211"

for model_num in (highest, lowest):
    assert validate(ops, model_num) is True
    print(model_num)
