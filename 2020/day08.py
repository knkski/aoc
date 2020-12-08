with open("day08.txt") as f:
    ops = [tuple(line.strip().split(" ")) for line in f.readlines()]


def run(lines) -> (str, int):
    """Returns accumulator value after loop or halt."""

    acc = 0
    current = 0
    seen = set()
    while True:
        if current >= len(lines):
            return "halt", acc
        if current in seen:
            return "loop", acc

        seen.add(current)
        op, val = lines[current]
        if op == "acc":
            acc += eval(val)
            current += 1
        elif op == "jmp":
            current += eval(val)
        elif op == "nop":
            current += 1
        else:
            raise Exception(f"Unknown op {op}")


# First run the instructions as-is, where they'll loop
print(run(ops)[1])

# Then brute-force switching each jmp/nop instruction to
# see if it halts
for i in range(len(ops)):
    modified = ops[:]
    op, _ = modified[i]
    if op == "acc":
        continue
    elif op == "nop":
        modified[i] = "jmp", modified[i][1]
    elif op == "jmp":
        modified[i] = "nop", modified[i][1]
    else:
        raise Exception(f"Unknown op {op}")

    result, acc = run(modified)
    if result == "halt":
        print(acc)
        break
