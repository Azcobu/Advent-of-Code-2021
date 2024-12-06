#AoC 24 Day 2a

def load_data() -> list:
    reports = []
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for line in infile.readlines():
            reports.append([int(x) for x in line.strip().split()])
    return reports

def main():
    safe = 0
    replist = load_data()

    for rep in replist:
        numrange = range(1, 4) if rep[0] < rep[1] else range(-1, -4, -1)
        for pos, x in enumerate(rep[:-1]):
            if rep[pos+1] - x not in numrange:
                break
        else:
            safe += 1

    print(safe)

if __name__ == '__main__':
    main()
