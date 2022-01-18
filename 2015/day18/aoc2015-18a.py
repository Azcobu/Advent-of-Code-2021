# AoC 2015 - Day 18a

def load_grid():
    grid = []
    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            grid.append([0 if x == '.' else 1 for x in line.strip()])
    return grid

def sum_neighbours(xpos, ypos, grid):
    total = 0
    n = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for poss in n:
        adjx, adjy = xpos + poss[0], ypos + poss[1]
        if 0 <= adjx <= len(grid[0]) - 1 and 0 <= adjy <= len(grid) - 1:
            total += grid[adjy][adjx]
    return total

def calc_steps(grid, numsteps):

    for step in range(numsteps):
        newgrid = []
        for ypos in range(len(grid)):
            newrow = []
            for xpos in range(len(grid[0])):
                currsum = sum_neighbours(xpos, ypos, grid)
                if grid[ypos][xpos] == 1:
                    newval = 1 if currsum in [2, 3] else 0
                else:
                    newval = 1 if currsum == 3 else 0
                newrow.append(newval)
            newgrid.append(newrow)
        grid = newgrid
    return newgrid

def sum_grid(grid):
    return sum([sum(x) for x in grid])

def main():
    grid = load_grid()
    newgrid = calc_steps(grid, 100)
    print(sum_grid(newgrid))

if __name__ == '__main__':
    main()
