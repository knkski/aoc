with open("day22.txt") as f:
    hands = [list(map(int, h.splitlines()[1:])) for h in f.read().split("\n\n")]


def play(hands, recursive=True):
    hands = [h[:] for h in hands]
    seen = set()
    while hands[0] and hands[1]:
        cards = (tuple(hands[0]), tuple(hands[1]))
        if cards in seen:
            return 0, hands[0]

        seen.add(cards)

        top1 = hands[0].pop(0)
        top2 = hands[1].pop(0)
        if recursive and top1 <= len(hands[0]) and top2 <= len(hands[1]):
            winner = play([hands[0][:top1], hands[1][:top2]])[0]
            if winner == 0:
                hands[0] += [top1, top2]
            else:
                hands[1] += [top2, top1]
        elif top1 > top2:
            hands[0] += [top1, top2]
        else:
            hands[1] += [top2, top1]

    if len(hands[0]):
        return 0, hands[0]
    else:
        return 1, hands[1]


hand = play(hands, recursive=False)[1]
print(sum(i * c for i, c in enumerate(reversed(hand), 1)))
hand = play(hands)[1]
print(sum(i * c for i, c in enumerate(reversed(hand), 1)))
