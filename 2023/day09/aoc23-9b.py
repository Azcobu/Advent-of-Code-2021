# AoC 2023 Day 9b

def load_data():
    with open('input.txt', 'r', encoding='utf-8') as infile:
        return [list(map(int, x.split())) for x in infile.readlines()]

def main():
    data = load_data()
    total = 0

    for line in data:
        currline = [line]
        while True:
            nextline = [num - line[pos] for pos, num in enumerate(line[1:])]
            currline.append(nextline)
            if set(nextline) != {0}:
                line = nextline
            else:
                currline[-1].append(0)
                currline.reverse()
                for linenum, line in enumerate(currline[1:]):
                    line.insert(0, line[0] - currline[linenum][0])
                total += currline[-1][0]
                break
    print(total)

if __name__ == '__main__':
    main()
