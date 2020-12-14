from itertools import count

with open("day13.txt") as f:
    lines = [line.strip() for line in f.readlines()]

start = int(lines[0])
busses = [int(i) for i in lines[1].split(",") if i != "x"]

for time in count(start):
    options = [b for b in busses if time % b == 0]
    if options:
        print(options[0] * (time - start))
        break

mods = [(i, int(n)) for i, n in enumerate(lines[1].split(",")) if n != "x"]
num = 0
step = 1
for remainder, mod in mods:
    while True:
        if (num + remainder) % mod == 0:
            break
        else:
            num += step
    step *= mod
print(num)
