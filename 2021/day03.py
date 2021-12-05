from operator import ge, lt

with open("day03.txt") as f:
    lines = [line.strip() for line in f.readlines()]

ones = [line.count("1") for line in zip(*lines)]
gamma = int("".join(map(lambda a: str(int(a > len(lines) / 2)), ones)), 2)
gamma2 = (1 << (len(bin(gamma)) - 1)) - 1
print(gamma * (gamma ^ gamma2))


def sift(nums, comparator, i=0):
    if len(nums) == 1:
        return int(nums[0], 2)
    else:
        ones = sum(n[i] == "1" for n in nums)

        wanted = "1" if comparator(ones, len(nums) / 2) else "0"
        return sift([n for n in nums if n[i] == wanted], comparator, i + 1)


print(sift(lines, comparator=ge) * sift(lines, comparator=lt))
