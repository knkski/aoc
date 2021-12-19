with open("day17.txt") as f:
    x, y = [map(int, x[2:].split("..")) for x in f.read().split(": ")[1].split(", ")]

xtarget = range(next(x), next(x) + 1)
ytarget = range(next(y), next(y) + 1)

highest = -1e9
successes = 0

for initx in range(-400, 400):
    for inity in range(-400, 400):
        posx = 0
        posy = 0
        velx = initx
        vely = inity
        highesty = 0
        for step in range(800):
            posx += velx
            posy += vely
            if posy > highesty:
                highesty = posy
            velx = velx - 1 if velx > 0 else (0 if velx == 0 else velx + 1)
            vely -= 1

            if posx in xtarget and posy in ytarget:
                if highesty > highest:
                    highest = highesty
                successes += 1
                break
            if posx > xtarget.stop:
                break
            if posy < ytarget.start:
                break

print(highest)
print(successes)
