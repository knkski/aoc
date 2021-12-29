from heapq import heappush, heappop

with open("day15.txt") as f:
    grid = {
        (i, j): int(item)
        for i, row in enumerate(f.readlines())
        for j, item in enumerate(row.strip())
    }


OFFSETS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def derisk(cave):
    queue = [(0, (0, 0))]
    costs = {coord: 1e9 for coord in cave}

    while queue:
        cost, current = heappop(queue)

        if cost >= costs[current]:
            continue

        costs[current] = cost

        for m, n in OFFSETS:
            neighbor = current[0] + m, current[1] + n
            if neighbor in cave:
                heappush(queue, (cost + cave[neighbor], neighbor))

    return costs[max(costs)]


def grow_cave(cave):
    result = {k: v for k, v in cave.items()}
    size = max(cave.keys())

    for extra_row in range(5):
        for extra_col in range(5):
            for coord, risk_level in cave.items():
                new_coord = (
                    coord[0] + (size[0] + 1) * extra_row,
                    coord[1] + (size[1] + 1) * extra_col,
                )
                new_level = risk_level + extra_row + extra_col
                if new_level > 9:
                    new_level -= 9
                result[new_coord] = new_level

    return result


print(derisk(grid))
print(derisk(grow_cave(grid)))
