# AoC 2016 - Day 24a
from collections import deque
from itertools import permutations

def load_data():
    walls, nums = {}, {}
    with open('input.txt', 'r') as infile:
        for ypos, y_c in enumerate(infile.readlines()):
            for xpos, x_c in enumerate(y_c):
                if x_c == '#':
                    walls[(xpos, ypos)] = '#'
                elif x_c.isnumeric():
                    nums[x_c] = (xpos, ypos)
    return walls, nums

def find_dist(walls, x, y, t_x, t_y):
    queue = deque([(x, y, 0)])
    visited = {(x, y)}

    while queue:
        x, y, steps = queue.pop()
        if (x, y) == (t_x, t_y):
            return steps
        for d_x, d_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            n_x, n_y = x + d_x,  y + d_y
            if (n_x, n_y) not in walls and (n_x, n_y) not in visited:
                queue.appendleft((n_x, n_y, steps+1))
                visited.add((n_x, n_y))
    return -1

def precalc_dists(walls, nums):
    d = {x:{} for x in nums.keys()}
    for k, v in d.items():
        for nn in nums.keys():
            if nn != k and nn not in d[k]:
                dist = find_dist(walls, nums[k][0], nums[k][1], nums[nn][0], nums[nn][1])
                d[k][nn] = dist
                d[nn][k] = dist
    return d

def find_shortest(walls, nums):
    totals = {}
    dists = precalc_dists(walls, nums)

    for p in permutations([str(x) for x in range(1, len(nums))]):
        route = ''.join(['0'] + list(p) + ['0'])
        totals[route] = 0
        for pos, num in enumerate(route[:-1]):
            nextnum = route[pos+1]
            totals[route] += dists[num][nextnum]
    totals = sorted(totals.items(), key=lambda x:x[1])
    return totals[0]

def main():
    w, n = load_data()
    print(find_shortest(w, n))

if __name__ == '__main__':
    main()
