folds = ['fold along x=655',
'fold along y=447',
'fold along x=327',
'fold along y=223',
'fold along x=163',
'fold along y=111',
'fold along x=81',
'fold along y=55',
'fold along x=40',
'fold along y=27',
'fold along y=13',
'fold along y=6']

data = []

def fold_y(data, foldpos):
    newsheet = []
    for coord in data:
        if coord[1] > foldpos:
            dist_from_fold = coord[1] - foldpos
            newcoord = foldpos - dist_from_fold
            newsheet.append((coord[0], newcoord))
        else:
            newsheet.append((coord[0], coord[1]))
    return list(set(newsheet))

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

def print_map(data):
    grid = []
    max_x = 50 #max(coord[0] for coord in data)
    max_y = 8 # max(coord[1] for coord in data)
    for ypos, y in enumerate(range(max_y)):
        row = ''
        for xpos, x in enumerate(range(max_x)):
            if (x, y) in data:
                row += '#'
            else:
                row += '.'
        grid.append(row)
    print('\n'.join(grid))

def main():
    data = []
    with open('aoc-13-input.txt', 'r') as infile:
        for coord in infile.read().splitlines():
            x, y = coord.split(',')
            data.append((int(x), int(y)))

    for f in folds:
        part = f.partition('=')
        num = int(part[2])
        if part[0][-1] == 'x':
            data = fold_x(data, num)
        else:
            data = fold_y(data, num)

    print_map(data)

if __name__ == '__main__':
    main()
