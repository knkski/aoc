import re
from functools import reduce

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("day04.txt") as f:
    passports = f.read().split("\n\n")

passports = [p.replace("\n", " ").strip().split(" ") for p in passports]
passports = [dict([f.split(":") for f in p]) for p in passports]


def reducer(total, passport):
    hgt_rgx = r"^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$"
    try:
        conditions = [
            1920 <= int(passport["byr"]) <= 2002,
            2010 <= int(passport["iyr"]) <= 2020,
            2020 <= int(passport["eyr"]) <= 2030,
            re.match(hgt_rgx, passport["hgt"]) is not None,
            re.match(r"^#[a-f0-9]{6}$", passport["hcl"]) is not None,
            passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
            re.match(r"^[0-9]{9}$", passport["pid"]) is not None,
        ]

        return total + all(conditions)
    except KeyError:
        return total


print(len([p for p in passports if all(field in p for field in REQUIRED_FIELDS)]))
print(reduce(reducer, passports, 0))
