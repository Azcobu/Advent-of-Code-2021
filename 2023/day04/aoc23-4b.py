# AoC 2023 Day 4b

def main():
    total = 0
    cardscores = {}

    with open('input.txt', 'r', encoding='utf-8') as infile:
        for num, line in enumerate(infile.readlines()):
            win, _, have = line.partition(': ')[2].partition(' | ')
            win, have = [set(map(int, x.split())) for x in [win, have]]
            cardscores[num+1] = len(win & have)

    cardstack = list(cardscores.keys())
    while cardstack:
        currcard = cardstack.pop()
        total += 1
        cardstack += [x for x in range(currcard + 1, currcard + 1 + cardscores[currcard])]
    print(total)

if __name__ == '__main__':
    main()
