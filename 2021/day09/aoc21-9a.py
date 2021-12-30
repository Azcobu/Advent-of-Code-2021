# Advent of Code 2021 - 9a

def calc_risk(data):
    risk = 0
    for ypos, row in enumerate(data):
        for xpos, val in enumerate(row):
            neighbours = []
            poss = (ypos-1, xpos), (ypos+1, xpos), (ypos, xpos-1), (ypos, xpos+1)
            nears = [p for p in poss if 0 <= p[0] < len(data) and 0 <= p[1] < len(row)]
            for p in nears:
                neighbours.append(data[p[0]][p[1]])

            if val < min(neighbours):
                risk += 1 + int(val)
    return risk

def main():
    fname = 'aoc-9-input.txt'
    with open(fname, 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    print(calc_risk(data))

if __name__ == '__main__':
    main()
