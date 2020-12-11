from itertools import count, product

with open("day11.txt") as f:
    SEATS = [list(line.strip()) for line in f.readlines()]

OPTIONS = [
    (lambda: [1], 4),
    (lambda: count(1), 5),
]

COORDS = [coord for coord in product(range(-1, 2), range(-1, 2)) if any(coord)]


def convolve(seats, span, max_neighbors):
    convolved = [row[:] for row in seats]
    for row in range(len(seats)):
        for seat in range(len(seats[row])):
            if seats[row][seat] == ".":
                continue
            neighbors = []

            for r, s in COORDS:
                for offset in span():
                    j = row + offset * r
                    k = seat + offset * s
                    if not (0 <= j < len(seats) and 0 <= k < len(seats[row])):
                        break
                    if seats[j][k] in ("#", "L"):
                        neighbors.append(seats[j][k])
                        break

            if seats[row][seat] == "L" and "#" not in neighbors:
                convolved[row][seat] = "#"

            if seats[row][seat] == "#" and neighbors.count("#") >= max_neighbors:
                convolved[row][seat] = "L"

    return convolved


for options in OPTIONS:
    seats = [row[:] for row in SEATS]
    while True:
        convolved = convolve(seats, *options)
        if convolved == seats:
            break
        else:
            seats = convolved

    print("".join("".join(row) for row in convolved).count("#"))
