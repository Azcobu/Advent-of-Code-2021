# AoC 2022 Day 8a
from math import prod

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().splitlines()

def count_visible(grid):
    maxrow = len(grid)
    maxcol = len(grid[0])
    visible = 2 * maxrow + 2 * maxcol - 4
    highscore = 0

    for r in range(1, maxrow - 1):
        for c in range(1, maxcol - 1):
            views = []
            up = [grid[x][c] for x in range(r)][::-1]
            down = [grid[x][c] for x in range(r+1, maxrow)]
            left = [grid[r][x] for x in range(c)][::-1]
            right = [grid[r][x] for x in range(c+1, maxcol)]
            for seq in up, down, left, right:
                tmpview = 0
                for t in seq:
                    tmpview += 1
                    if t >= grid[r][c]:
                        break
                views.append(tmpview)
            highscore = max(prod(views), highscore)          
    return highscore
               
def main():
    print(count_visible(load_data()))

if __name__ == '__main__':
    main()
