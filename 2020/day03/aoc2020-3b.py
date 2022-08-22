import math

def load_data():
    grid = set()
    with open('input.txt', 'r') as infile:
        for y, line in enumerate([x.strip() for x in infile.readlines()]):
            for x, char in enumerate(line):
                if char == '#':
                    grid.add((x, y))
    return grid

def count_trees(grid):
    slopes = {k:0 for k in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]}
    max_x = max([y[0] for y in grid])
    max_y = max([y[1] for y in grid])

    for slope in slopes.keys():
        trees = 0
        curr_x, curr_y = 0, 0
        while curr_y <= max_y:
            curr_x += slope[0]
            if curr_x > max_x:
                curr_x = curr_x % max_x - 1
            curr_y += slope[1]
            if (curr_x, curr_y) in grid:
                trees += 1
        slopes[slope] = trees
    
    return math.prod(slopes.values())

def main():
    print(count_trees(load_data()))

if __name__ == '__main__':
    main()
