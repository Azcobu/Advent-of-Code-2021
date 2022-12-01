# AoC 2022 Day 1a

def load_data():
    cals = []
    currsum = 0

    with open('input.txt', 'r') as infile:
        c = infile.readlines()
    for line in c:
        if line == '\n':
            cals.append(currsum)
            currsum = 0
        else:
            currsum += int(line.strip())
    return cals

def main():
    c = load_data()
    print(sorted(c)[-1])

if __name__ == '__main__':
    main()
