# AoC 2023 - Day 16b

def load_data():
    grid = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, char in enumerate(row.strip()):
                grid[(colnum, rownum)] = char
    return grid

def calc_energized(startdir, startpos, grid):
    mirrors = {'/': {'N': 'E', 'W': 'S', 'S': 'W', 'E': 'N'},
              '\\': {'N': 'W', 'W': 'N', 'S': 'E', 'E': 'S'}}
    dirs = {'N': (0, -1), 'W': (-1, 0), 'S': (0, 1), 'E': (1, 0)}
    q = [(startdir, startpos)]
    energized = set()

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

    return len(set([x[1] for x in energized]))

def main():
    grid = load_data()
    maxcol = max([x[0] for x in grid]) + 1
    maxrow = max([x[1] for x in grid]) + 1

    n = [calc_energized('N', (k, maxrow + 1), grid) for k in range(maxcol)]
    s = [calc_energized('S', (k, -1), grid) for k in range(maxcol)]
    w = [calc_energized('W', (maxcol + 1, k), grid) for k in range(maxrow)]
    e = [calc_energized('E', (-1, k), grid) for k in range(maxrow)]

    print(max(n + s + e + w))

if __name__ == '__main__':
    main()
