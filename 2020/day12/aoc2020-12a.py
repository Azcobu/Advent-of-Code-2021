# AoC 2020 Day 12a

def load_data():
    instrs = []
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    for line in d:
        instrs.append((line[0], int(line[1:])))
    return instrs

def navigate(instrs):
    pos = [0, 0]
    points = ['N', 'E', 'S', 'W']
    dirs = {x[0]: x[1] for x in zip(points, [(0, 1), (1, 0), (0, -1), (-1, 0)])}
    bearing = 'E'

    for action, num in instrs:
        if action in points or action == 'F':
            if action == 'F':
                action = bearing
            pos[0] += num * dirs[action][0]
            pos[1] += num * dirs[action][1]
        else:
            if action == 'L':
                num *= -1
            jump = (points.index(bearing) + num // 90) % 4
            bearing = points[jump]
    return abs(pos[0]) + abs(pos[1])
            
def main():
    print(navigate(load_data()))

if __name__ == '__main__':
    main()
