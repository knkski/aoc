from functools import reduce

with open("day10.txt") as f:
    lines = [line.strip() for line in f.readlines()]


invalid = 0
incomplete = []
for line in lines:
    stack = []
    for ch in line:
        last = stack[-1] if stack else None
        match [ch, last]:
            case ['(', _] | ['[', _] | ['{', _] | ['<', _]:
                stack.append(ch)
            case [')', '(']:
                stack.pop()
            case [')', _]:
                invalid += 3
                break
            case [']', '[']:
                stack.pop()
            case [']', _]:
                invalid += 57
                break
            case ['}', '{']:
                stack.pop()
            case ['}', _]:
                invalid += 1197
                break
            case ['>', '<']:
                stack.pop()
            case ['>', _]:
                invalid += 25137
                break
            case other:
                raise ValueError(other)
    else:
        if len(stack):
            incomplete.append(stack)

print(invalid)


def score(memo, ch):
    return memo * 5 + ' ([{<'.find(ch)


scores = list(sorted(reduce(score, reversed(stack), 0) for stack in incomplete))
print(scores[len(scores)//2])
