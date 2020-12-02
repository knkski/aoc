from collections import Counter
from itertools import count
import re

with open('day20.txt') as f:
    lines = f.readlines()


def parse(line):
    nums = list(map(int, re.findall(r'[\d-]+', line)))

    return {
        'position': nums[:3],
        'velocity': nums[3:6],
        'acceleration': nums[6:],
    }


def sum_abs(vec):
    return sum(map(abs, vec))


def simulate(particles, remove_collisions=False):
    for _ in count():
        min_acceleration = min(sum_abs(p['acceleration']) for p in particles)

        for i, particle in enumerate(particles):
            particle['velocity'][0] += particle['acceleration'][0]
            particle['velocity'][1] += particle['acceleration'][1]
            particle['velocity'][2] += particle['acceleration'][2]

            particle['position'][0] += particle['velocity'][0]
            particle['position'][1] += particle['velocity'][1]
            particle['position'][2] += particle['velocity'][2]

        index, min_particle = min(enumerate(particles), key=lambda x: tuple(map(sum_abs, x[1].values())))

        if sum_abs(min_particle['acceleration']) == min_acceleration:
            return len(particles) if remove_collisions else index

        if remove_collisions:
            dupes = Counter([tuple(p['position']) for p in particles])
            particles = [p for p in particles if dupes[tuple(p['position'])] == 1]


print(simulate([parse(line) for line in lines]))
print(simulate([parse(line) for line in lines], remove_collisions=True))
