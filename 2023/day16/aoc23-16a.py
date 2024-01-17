# AoC 2023 - Day 16a

def load_data():
    grid = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, char in enumerate(row.strip()):
                grid[(colnum, rownum)] = char
    return grid

def main():
    mirrors = {'/': {'N': 'E', 'W': 'S', 'S': 'W', 'E': 'N'},
              '\\': {'N': 'W', 'W': 'N', 'S': 'E', 'E': 'S'}}
    dirs = {'N': (0, -1), 'W': (-1, 0), 'S': (0, 1), 'E': (1, 0)}
    q = [('E', (-1, 0))]
    energized = set()
    grid = load_data()

    while q:
        bdir, bpos = q.pop()
        nx, ny = bpos[0] + dirs[bdir][0], bpos[1] + dirs[bdir][1]

        if (nx, ny) not in grid or (bdir, (nx, ny)) in energized:
            continue

        newchar = grid[(nx, ny)]
        energized.add((bdir, (nx, ny)))

        match newchar:
            case '\\' | '/':
                bdir = mirrors[newchar][bdir]
                q.append((bdir, (nx, ny)))
            case '-' if bdir in 'NS':
                q.append(('E', (nx, ny)))
                q.append(('W', (nx, ny)))
            case '|' if bdir in 'EW':
                q.append(('N', (nx, ny)))
                q.append(('S', (nx, ny)))
            case _:
                q.append((bdir, (nx, ny)))

    print(len(set([x[1] for x in energized])))

if __name__ == '__main__':
    main()
