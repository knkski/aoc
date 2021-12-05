with open("day04.txt") as f:
    data = f.read()

nums = [int(n) for n in data.splitlines()[0].split(",")]


def get_boards():
    return [
        [[int(i) for i in row.split(" ") if i] for row in b.splitlines()]
        for b in data.split("\n\n")[1:]
    ]


def is_winner(board):
    if any(not any(row) for row in board):
        return True

    if any(not any(col) for col in zip(*board)):
        return True

    return False


def get_best(boards):
    for num in nums:
        for board in boards:
            board[:] = [[item if item != num else None for item in row] for row in board]

            if is_winner(board):
                return sum(j for row in board for j in row if j) * int(num)


def get_worst(boards, ns):
    losers = []
    for board in boards:
        board[:] = [[item if item != ns[0] else None for item in row] for row in board]

        if not is_winner(board):
            losers.append(board)

    if len(losers) == 0:
        return sum(j for row in boards[0] for j in row if j and j != ns[0]) * ns[0]
    return get_worst(losers, ns[1:])


print(get_best(get_boards()))
print(get_worst(get_boards(), nums))
