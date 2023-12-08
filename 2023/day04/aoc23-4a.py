# AoC 2023 Day 4a

def main():
    total = 0
    with open('input.txt', 'r', encoding='utf-8') as infile:
        data = infile.readlines()
    for num, line in enumerate(data):
        win, _, have = line.partition(': ')[2].partition(' | ')
        win, have = [set(map(int, x.split())) for x in [win, have]]
        if wincards := len(win & have):
            total += 2 ** (wincards - 1)
    print(total)

if __name__ == '__main__':
    main()
