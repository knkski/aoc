from functools import lru_cache
from itertools import cycle, islice, count

with open("day21.txt") as f:
    pos1, pos2 = [int(line.strip().split(': ')[1]) for line in f.readlines()]

def play1():
    state = {
        'turn': '1',
        '1': {
            'position': pos1 - 1,
            'score': 0,
        },
        '2': {
            'position': pos2 - 1,
            'score': 0,
        }
    }
    die = cycle(range(1, 101))
    for turns in count(1):
        roll = sum(islice(die, 3))
        player = state[state['turn']]
        player['position'] = (player['position'] + roll) % 10
        player['score'] += player['position'] + 1
        state['turn'] = '2' if state['turn'] == '1' else '1'

        if player['score'] >= 1000:
            return 3 * turns * state[state['turn']]['score']

rolled = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@lru_cache(maxsize=None)
def play2_helper(rolls, turn, pos1, score1, pos2, score2):
    position, score = (pos1, score1) if turn == '1' else (pos2, score2)
    position = (position + rolls) % 10

    score += position + 1
    if score >= 21:
        return turn == '1'

    if turn == '1':
        args = position, score, pos2, score2
    else:
        args = pos1, score1, position, score

    next_turn = '1' if turn == '2' else '2'

    return sum(
        rolled[n] * play2_helper(
            n,
            next_turn,
            *args
        )
        for n in (3, 4, 5, 6, 7, 8, 9)
    )


def play2():
    return sum(
        rolled[n] * play2_helper(
            n,
            '1',
            pos1 - 1,
            0,
            pos2 - 1,
            0
        )
        for n in (3, 4, 5, 6, 7, 8, 9)
    )


print(play1())
print(play2())
