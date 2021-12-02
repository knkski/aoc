with open("day02.txt") as f:
    lines = [line.strip().split(" ") for line in f.readlines()]


def go():
    x1 = 0
    y1 = 0

    x2 = 0
    y2 = 0
    aim = 0

    for direction, num in lines:
        num = int(num)
        if direction == "forward":
            x1 += num
            x2 += num
            y2 += num * aim
        elif direction == "up":
            y1 -= num
            aim -= num
        elif direction == "down":
            y1 += num
            aim += num

    return x1 * y1, x2 * y2


print("\n".join(map(str, go())))
