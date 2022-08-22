
def load_data():
    grid = set()
    with open('input.txt', 'r') as infile:
        for y, line in enumerate([x.strip() for x in infile.readlines()]):
            for x, char in enumerate(line):
                if char == '#':
                    grid.add((x, y))
    return grid

def count_trees(grid):
    curr_x, curr_y = 0, 0
    steps = 3, 1
    max_x = max([y[0] for y in grid])
    max_y = max([y[1] for y in grid])
    trees = 0

    while curr_y <= max_y:
        curr_x += steps[0]
        if curr_x > max_x:
            curr_x = curr_x % max_x - 1
        curr_y += steps[1]
        if (curr_x, curr_y) in grid:
            trees += 1
    return trees

def main():
    print(count_trees(load_data()))

if __name__ == '__main__':
    main()
