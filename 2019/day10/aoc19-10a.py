# AoC 2019 Day 10a
import math

def load_data():
    grid = set()
    with open('example1.txt', 'r') as infile:
        for y, line in enumerate([x.strip() for x in infile.readlines()]):
            for x, char in enumerate(line):
                if char == '#':
                    grid.add((x, y))
    return grid

def count_visible(grid, x, y):
    visible = 0
    for ast in grid:
        if ast == (x, y): continue
        

def find_most_visible(grid):
    vis = {}
    for ast in grid:
        vis[ast] = count_visible(grid, *ast)
    print(sorted(vis.items(), key=lambda x: x[1], reverse=True))

def main():
    grid = load_data()
    print(find_most_visible(grid))

if __name__ == '__main__':
    main()
