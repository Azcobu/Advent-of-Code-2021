# AoC 2020 Day 12b

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
    waypoint = [10, 1]

    for action, num in instrs:
        if action in points:
            waypoint[0] += num * dirs[action][0]
            waypoint[1] += num * dirs[action][1]
        elif action in ['L', 'R']:
            if action == 'L':
                num = 360 - num
            for turn in range(num // 90):
                waypoint = [waypoint[1], -waypoint[0]]
        else:
            pos[0] += waypoint[0] * num
            pos[1] += waypoint[1] * num

    return abs(pos[0]) + abs(pos[1])
            
def main():
    print(navigate(load_data()))

if __name__ == '__main__':
    main()
