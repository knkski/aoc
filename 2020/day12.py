from math import sin, cos, radians

with open("day12.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def calc1(commands):
    facing = 0
    position = [0, 0]

    for command in commands:
        cmd, num = command[0], int(command[1:])

        if cmd == "N":
            position[0] -= num
        elif cmd == "S":
            position[0] += num
        elif cmd == "E":
            position[1] += num
        elif cmd == "W":
            position[1] -= num
        elif cmd == "L":
            facing += num
        elif cmd == "R":
            facing -= num
        elif cmd == "F":
            position[0] -= num * int(sin(radians(facing)))
            position[1] += num * int(cos(radians(facing)))
        else:
            raise Exception(f"Unknown command {cmd}")

    return sum(map(abs, position))


def calc2(commands):
    position = [0, 0]
    waypoint = [-1, 10]

    for command in commands:
        cmd, num = command[0], int(command[1:])

        if cmd == "N":
            waypoint[0] -= num
        elif cmd == "S":
            waypoint[0] += num
        elif cmd == "E":
            waypoint[1] += num
        elif cmd == "W":
            waypoint[1] -= num
        elif cmd == "L":
            if num == 0:
                pass
            elif num == 90:
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
            elif num == 180:
                waypoint[0] = -waypoint[0]
                waypoint[1] = -waypoint[1]
            elif num == 270:
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
            else:
                0 / 0
        elif cmd == "R":
            if num == 0:
                pass
            elif num == 90:
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
            elif num == 180:
                waypoint[0] = -waypoint[0]
                waypoint[1] = -waypoint[1]
            elif num == 270:
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
            else:
                0 / 0
        elif cmd == "F":
            position[0] += num * waypoint[0]
            position[1] += num * waypoint[1]
        else:
            raise Exception(f"Unknown command {cmd}")

    return sum(map(abs, position))


print(calc1(lines))
print(calc2(lines))
