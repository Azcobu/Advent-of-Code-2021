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
        if ast != (x, y):
            step_x, step_y = ast[0] - x, ast[1] - y
            
    return visible

def find_most_visible(grid):
    max_visible = 0
    max_x, max_y = 0, 0
    for ast in grid:
        visible = count_visible(grid, *ast)
        if visible > max_visible:
            max_visible = visible
            max_x, max_y = ast[0], ast[1]
    return max_x, max_y, max_visible

def main():
    grid = load_data()
    print(find_most_visible(grid))

if __name__ == '__main__':
    main()
