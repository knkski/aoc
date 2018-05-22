from collections import defaultdict

tape = defaultdict(int)
cursor = 0

state = 'A'

for _ in range(12964419):
    value = tape[cursor]

    if state == 'A':
        if value == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'B'
        elif value == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'F'
        else:
            0/0

    elif state == 'B':
        if value == 0:
            tape[cursor] = 0
            cursor -= 1
            state = 'B'
        elif value == 1:
            tape[cursor] = 1
            cursor -= 1
            state = 'C'
        else:
            0/0

    elif state == 'C':
        if value == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'D'
        elif value == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'C'
        else:
            0/0

    elif state == 'D':
        if value == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'E'
        elif value == 1:
            tape[cursor] = 1
            cursor += 1
            state = 'A'
        else:
            0/0

    elif state == 'E':
        if value == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'F'
        elif value == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'D'
        else:
            0/0

    elif state == 'F':
        if value == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'A'
        elif value == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'E'
        else:
            0/0
    else:
        0 / 0


print(sum(tape.values()))
