from functools import reduce

num = 337

def part1(memo, i):
    buffer, current = memo
    current = (current + num) % i + 1

    buffer.insert(current, i)

    return buffer, current

buffer = reduce(part1, range(1, 2018), ([0], 0))[0]

print(buffer[buffer.index(2017) + 1])

def part2(memo, i):
    current, second_element = memo
    current = (current + num) % i + 1

    return current, i if current == 1 else second_element

print(reduce(part2, range(1, 50000001), (0, 0))[1])
