# AoC 2022 Day 8a

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().splitlines()

def count_visible(grid):
    maxrow = len(grid)
    maxcol = len(grid[0])
    visible = 2 * maxrow + 2 * maxcol - 4

    for r in range(1, maxrow - 1):
        for c in range(1, maxcol - 1):
            up = [grid[x][c] for x in range(r)]
            down = [grid[x][c] for x in range(r+1, maxrow)]
            left = [grid[r][x] for x in range(c)]
            right = [grid[r][x] for x in range(c+1, maxcol)]
            for seq in up, down, left, right:
                if all(grid[r][c] > x for x in seq):
                    visible += 1
                    break
    return visible
               
def main():
    print(count_visible(load_data()))

if __name__ == '__main__':
    main()
