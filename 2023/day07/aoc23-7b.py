# AoC 223 Day 7b
from collections import Counter
from functools import cmp_to_key

def load_data():
    with open('input.txt', 'r', encoding='utf-8') as infile:
        return [(x.split()[0], int(x.split()[1])) for x in infile.readlines()]

def classify(hand):
    five_kind = lambda f, s: f == 5
    four_kind = lambda f, s: f == 4
    full_house = lambda f, s: f == 3 and s == 2
    three_kind = lambda f, s: f == 3 and s == 1
    two_pair = lambda f, s: f == 2 and s == 2
    pair = lambda f, s: f == 2 and s == 1
    highcard = lambda f, s: f == 1

    if 'J' in hand:
        nojs = [x for x in hand if x != 'J']
        if nojs:
            commcard = Counter(nojs).most_common(1)[0][0]
            hand = ''.join([commcard if x == 'J' else x for x in hand])

    c = Counter(hand)
    first = c.most_common()[0][1]
    sec = c.most_common()[1][1] if first < 5 else 0

    for rank, func in enumerate([five_kind, four_kind, full_house, three_kind, two_pair, pair, highcard]):
        if func(first, sec):
            return rank

def cmporder(h1, h2):
    order = {char:pos for pos, char in enumerate([x for x in 'AKQT98765432J'])}
    for cardcomp in zip(h1[0], h2[0]):
        if order[cardcomp[0]] < order[cardcomp[1]]:
            return -1
        if order[cardcomp[0]] > order[cardcomp[1]]:
            return 1
    return 0

def main():
    hands = [(hand, bid, classify(hand)) for hand, bid in load_data()]
    k = sorted(hands, key=cmp_to_key(cmporder))
    k = sorted(k, key=lambda x: x[2])[::-1]
    total = sum([(num + 1) * x[1] for num, x in enumerate(k)])
    print(total)

if __name__ == '__main__':
    main()
