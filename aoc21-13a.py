data = []

def fold_x(data, foldpos):
    newsheet = []
    for coord in data:
        if coord[0] > foldpos:
            dist_from_fold = coord[0] - foldpos
            newcoord = foldpos - dist_from_fold
            newsheet.append((newcoord, coord[1]))
        else:
            newsheet.append((coord[0], coord[1]))
    return list(set(newsheet))

def main():
    data = []
    with open('aoc-13-input.txt', 'r') as infile:
        for coord in infile.read().splitlines():
            x, y = coord.split(',')
            data.append((int(x), int(y)))

    data = fold_x(data, 655)
    print(len(data))

if __name__ == '__main__':
    main()
