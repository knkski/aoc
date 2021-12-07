from collections import Counter

with open("day07.txt") as f:
    nums = Counter(map(int, f.read().strip().split(",")))


def light(i, count, pos):
    return count * abs(i - pos)


def heavy(i, count, pos):
    n = abs(i - pos)
    return count * (n * (n + 1) // 2)


print(min(sum(light(i, count, pos) for i, count in nums.items()) for pos in range(0, max(nums))))
print(min(sum(heavy(i, count, pos) for i, count in nums.items()) for pos in range(0, max(nums))))
