# AoC 2020 Day 22b

def load_data():
    hands = {1: [], 2: []}
    with open('input.txt', 'r') as infile:
        d = infile.read().split('\n\n')
    for hand in d:
        h = hand.split('\n')
        p = int(h[0][7])
        hands[p] = [int(x) for x in h[1:] if x.strip()]
    return hands

def eval_cards(hands):
    while True:
        a, b = hands[1].pop(0), hands[2].pop(0)
        if a > b:
            hands[1] += [a, b]
        else:
            hands[2] += [b, a]
        if not len(hands[1]) or not len(hands[2]):
            break
    
    final = hands[1] if len(hands[1]) else hands[2]
    return sum([(mult + 1) * card for mult, card in enumerate(final[::-1])])

def main():
    print(eval_cards(load_data()))

if __name__ == '__main__':
    main()
