with open('day9.txt') as f:
    data = f.read()

total = 0
total_garbage = 0

current_depth = 0
in_garbage = False
cancelled = False

for char in data:
    if cancelled:
        cancelled = False
        continue

    if in_garbage and char not in '!>':
        total_garbage += 1

    if char == '{' and not in_garbage:
        current_depth += 1
        total += current_depth
    elif char == '}' and not in_garbage:
        current_depth -= 1
    elif char == '<':
        in_garbage = True
    elif char == '>':
        in_garbage = False
    elif char == '!':
        cancelled = True

print(total)
print(total_garbage)
