# AoC 2022 Day 12
from collections import deque

def load_data():
    grid = {}
    with open('input.txt', 'r') as infile:
        d = infile.readlines()
    for rownum, line in enumerate(d):
        for colnum, char in enumerate(line.strip()):
            grid[(colnum, rownum)] = char
    return grid
    
def find_path(grid):
    start_x, start_y = [k for k, v in grid.items() if v == 'E'][0]
    queue = deque([(start_x, start_y, 0)])
    visited = {(start_x, start_y)}

    while queue:
        x, y, steps = queue.popleft()
        if grid[(x, y)] == 'a':
            return steps
        else:
            for d_x, d_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + d_x, y + d_y
                if (new_x, new_y) in grid and (new_x, new_y) not in visited:
                    if ord(grid[(new_x, new_y)]) >= ord(grid[(x, y)]) - 1:
                        queue.append((new_x, new_y, steps + 1))
                        visited.add((new_x, new_y))
    return -1

def main():
    print(find_path(load_data()))

if __name__ == '__main__':
    main()
