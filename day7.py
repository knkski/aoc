import re

with open('day7.txt') as f:
    programs = f.readlines()

# Turn programs into a dict that looks like this:
# {
#     'foo': {
#         'weight': 42,
#         'children': ['bar', 'baz'],
#     },
#     ...
# }

def parse(program):
    # Thanks to llimllib for this
    name, weight, *children = re.findall('(\w+)', program)

    return (name, {
        'weight': int(weight),
        'children': children,
    })

programs = dict(
    parse(p)
    for p in programs
)

# Grab the complete list of children, and then calculate the root node
# by checking which one doesn't appear in that list
children = set(child for p in programs.values() for child in p['children'])

root = set(programs.keys()).difference(children).pop()

print(root)

# Given lists of child names and weights, calculates the bad child and
# what the correct weight for it should be.
def get_correct_weight(names, weights):
    bad_weight = next(
        w
        for w in weights
        if weights.count(w) == 1
    )

    good_weight = weights[weights.index(bad_weight) + 1 % len(weights)]

    adjustment = good_weight - bad_weight

    bad_child = names[weights.index(bad_weight)]
    bad_child_weight = programs[bad_child]['weight']

    print(bad_child_weight + adjustment)


def find_incorrect_weight(name):
    program = programs[name]

    if not program['children']:
        return program['weight']

    child_weights = [find_incorrect_weight(child) for child in program['children']]

    # If the list of weights are not identical, we've found the incorrect node.
    # Since this is recursive and we want to stop the first time we encounter
    # this imbalance, raise a StopIteration to drop everything and return.
    if len(set(child_weights)) != 1:
        get_correct_weight(program['children'], child_weights)
        raise StopIteration()

    return program['weight'] + sum(child_weights)

try:
    find_incorrect_weight(root)
except StopIteration:
    pass
