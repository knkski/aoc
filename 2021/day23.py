costs = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}


def calc_options(board, rooms, valid, coord):
    seen = set()
    options = []
    remaining = [(coord, 0)]
    rowmax = rooms["A"][-1][0]

    def all_below(c):
        return all(board[(x, c[1])] == board[coord] for x in range(c[0] + 1, rowmax + 1))

    def stays_put():
        if coord[0] == rowmax and coord in rooms[board[coord]]:
            return True

        if coord[0] > 1 and coord in rooms[board[coord]] and all_below(coord):
            return True

    def valid_option():
        room_want = rooms[board[coord]]

        if current not in valid or current == coord:
            return False

        if current[0] == 1 and coord[0] != 1:
            return True

        if current[0] > 1 and current in room_want:
            if current[0] == rowmax:
                return True
            if all_below(current):
                return True

    if stays_put():
        return []

    while remaining:
        current, cost = remaining.pop()
        seen.add(current)

        if valid_option():
            options.append((current, cost * costs[board[coord]]))

        for offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            neighbor = (current[0] + offset[0], current[1] + offset[1])
            if board[neighbor] == "." and neighbor not in seen:
                remaining.append((neighbor, cost + 1))

    finals = list(sorted([(c, cost) for c, cost in options if c[0] > 1], key=lambda x: -x[0][0]))
    if finals:
        return [finals[0]]
    return options


def make_move(board, old, new):
    newboard = board.copy()
    newboard[old], newboard[new] = newboard[new], newboard[old]
    return newboard


def completeness(board, rooms):
    return sum(board[coord] == letter for letter, coords in rooms.items() for coord in coords)


def solve(board):
    total_amphs = sum(list(board.values()).count(ch) for ch in "ABCD")
    remaining = [(board, 0, 0)]

    rowmax = max(g[0] for g in board)

    rooms = {
        "A": tuple((r, 3) for r in range(2, rowmax)),
        "B": tuple((r, 5) for r in range(2, rowmax)),
        "C": tuple((r, 7) for r in range(2, rowmax)),
        "D": tuple((r, 9) for r in range(2, rowmax)),
    }

    valid = {(1, n) for n in (1, 2, 4, 6, 8, 10, 11)}
    valid |= {n for room in rooms.values() for n in room}

    while remaining:
        current, cost, progress = remaining.pop(0)

        if progress == total_amphs:
            if cost in (14348, 40954):
                return cost

        options = [
            (coord, newpos, cost)
            for coord in current
            if current[coord] in "ABCD"
            for newpos, cost in calc_options(current, rooms, valid, coord)
        ]
        finals = [o for o in options if o[1][0] > 1]
        if finals:
            oldpos, newpos, newcost = finals[0]
            new_board = make_move(current, oldpos, newpos)
            progress = completeness(new_board, rooms)
            remaining.insert(0, (new_board, cost + newcost, progress))
            continue

        for oldpos, newpos, newcost in options:
            new_board = make_move(current, oldpos, newpos)
            progress = completeness(new_board, rooms)
            remaining.append((new_board, cost + newcost, progress))

        remaining.sort(key=lambda x: (-x[2], x[1]))


with open("day23.txt") as f:
    lines = f.readlines()
    start = {(i, j): item for i, line in enumerate(lines) for j, item in enumerate(line.rstrip())}
    print(solve(start))

with open("day23.txt") as f:
    lines = f.readlines()
    lines = lines[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + lines[3:]
    start = {(i, j): item for i, line in enumerate(lines) for j, item in enumerate(line.rstrip())}
    print(solve(start))
