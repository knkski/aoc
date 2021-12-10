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
            case _:
                0/0
    else:
        if len(stack):
            incomplete.append(stack)

print(invalid)

scores = []
for stack in incomplete:
    score = 0
    for ch in reversed(stack):
        score *= 5
        match ch:
            case '(':
                score += 1
            case '[':
                score += 2
            case '{':
                score += 3
            case '<':
                score += 4
            case _:
                0/0
    scores.append(score)
scores.sort()

print(scores[len(scores)//2])
