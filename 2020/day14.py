import re
from functools import reduce


def parse(line):
    if line.startswith("mask = "):
        return (line[7:],)
    else:
        mem, val = re.match(r"mem\[(\d+)\] = (\d+)", line).groups()
        return int(mem), int(val)


with open("day14.txt") as f:
    instructions = [parse(line.strip()) for line in f.readlines()]


def expand_mask(mask):
    count = mask.count("X")

    # Generate a bitstring for each value of [0, 2**count]. Then,
    # scatter each bit in the string amongst each `X` in the input mask.
    return [
        [next(magic) if char == "X" else char if char == "1" else None for char in mask]
        for i in range(2 ** count)
        if (magic := iter("{0:0{1}b}".format(i, count)))
    ]


def reducer1(memo, instruction):
    memory, mask = memo
    if len(instruction) == 1:
        mask = instruction[0]
    else:
        mem, val = instruction
        for i, bit in enumerate(reversed(mask)):
            if bit == "1":
                val |= 1 << i
            elif bit == "0":
                val &= ~(1 << i)
        memory[mem] = val
    return memory, mask


def reducer2(memo, instruction):
    memory, mask = memo
    if len(instruction) == 1:
        mask = instruction[0]
    else:
        for submask in expand_mask(mask):
            mem, val = instruction
            for i, bit in enumerate(reversed(submask)):
                if bit == "1":
                    mem |= 1 << i
                elif bit == "0":
                    mem &= ~(1 << i)
            memory[mem] = val
    return memory, mask


for reducer in (reducer1, reducer2):
    memory, _ = reduce(reducer, instructions, ({}, 0))
    print(sum(memory.values()))
