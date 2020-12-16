from math import prod

with open("day16.txt") as f:
    fields, mine, nearby = f.read().split("\n\n")


def parse_field(field):
    name, val = field.split(":")
    return name, [
        (int(span.split("-")[0]), int(span.split("-")[1]) + 1)
        for span in val.strip().split(" or ")
    ]


fields = dict(map(parse_field, fields.splitlines()))
mine = [int(n) for n in mine.splitlines()[1].split(",")]
nearby = [[int(n) for n in t.split(",")] for t in nearby.splitlines()[1:]]


def valid(num):
    return any(num in range(*span) for spans in fields.values() for span in spans)


errors = [num for ticket in nearby for num in ticket if not valid(num)]

print(sum(errors))

valid_nearby = [ticket for ticket in nearby if all(valid(num) for num in ticket)]

field_options = [
    (
        nums[0],
        [
            field
            for field, spans in fields.items()
            if all(f in range(*spans[0]) or f in range(*spans[1]) for f in nums)
        ],
    )
    for i, nums in enumerate(zip(*[mine] + valid_nearby))
]

solved_ticket = {}

for value, options in sorted(field_options, key=lambda x: len(x[1])):
    field = next(o for o in options if o not in solved_ticket)
    solved_ticket[field] = value

print(prod(v for k, v in solved_ticket.items() if k.startswith("departure")))
