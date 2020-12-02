from functools import reduce

with open('day1.txt') as f:
    numbers = [int(n) for n in f.read().replace('\n', '')]

def circular_sum(offset=1):
    def reducer(memo, nums):
        if nums[0] == nums[1]:
            return memo + nums[0]
        else:
            return memo
    return reduce(reducer, zip(numbers, numbers[offset:] + numbers[:offset]), 0)

print(circular_sum())
print(circular_sum(offset=len(numbers)//2))
