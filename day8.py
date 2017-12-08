from operator import add, sub
from collections import defaultdict

with open('day8_input.txt') as f:
    instructions = f.readlines()

registers = defaultdict(int)
highest = 0
operators = {
    'inc': add,
    'dec': sub,
}

for instruction in instructions:
    register, operator, amount, _, if_register, if_operator, if_amount = instruction.split(' ')

    if registers.values() and max(registers.values()) > highest:
        highest = max(registers.values())

    if eval(f'registers["{if_register}"] {if_operator} {if_amount}'):
        registers[register] = operators[operator](registers[register], int(amount))

print(max(registers.values()))
print(highest)
