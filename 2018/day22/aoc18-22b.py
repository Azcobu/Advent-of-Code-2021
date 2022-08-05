# AoC 2018 Day 22b
from queue import PriorityQueue

def calc_erosion(x, y, cave, depth, target):
    if x == y == 0 or (x, y) == target:
        geo_index = 0
    elif x == 0:
        geo_index = y * 48271
    elif y == 0:
        geo_index = x * 16807
    else:
        geo_index = cave[(x-1, y)] * cave[(x, y-1)]
    return (geo_index + depth) % 20183

def gen_cave(depth, target):
    extra_boundary = 50
    tmpcave, cave = {}, {}
    for y in range(target[1] + extra_boundary):
        for x in range(target[0] + extra_boundary):
            tmpcave[(x, y)] = calc_erosion(x, y, tmpcave, depth, target)
            cave[(x, y)] = tmpcave[(x, y)] % 3
    cave[target] = 0
    return cave

def find_min_path(cave, target):
    # for moving between types X and Y, only tool Z is valid
    visited, unvisited = {}, PriorityQueue()
    
    unvisited.put((0, (0, 0, 1))) # time, (x, y, tool)
   
    while not unvisited.empty():
        time, (x, y, tool) = unvisited.get()
        env = cave[(x, y)]

        if (x, y, tool) == (target[0], target[1], 1):
            return time

        if (x, y, tool) in visited and visited[(x, y, tool)] <= time:
            continue  

        visited[(x, y, tool)] = time            
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in cave and (nx, ny, tool) not in visited:
                new_env = cave[(nx, ny)]
                if new_env == env or (new_env != env and new_env != tool):
                    unvisited.put((time + 1, (nx, ny, tool)))
                elif env != new_env:
                    newtool = [x for x in [0, 1, 2] if x != env and x != new_env][0]
                    unvisited.put((time + 8, (nx, ny, newtool)))

def main():
    cave = gen_cave(510, (10, 10))
    print(find_min_path(cave, (10, 10)))
    cave = gen_cave(11394, (7, 701))
    print(find_min_path(cave, (7, 701)))

if __name__ == '__main__':
    main()
