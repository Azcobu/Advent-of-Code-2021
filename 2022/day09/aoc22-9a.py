# AoC 2022 Day 9a

def load_data():
    with open('input.txt', 'r') as infile:
        return [(x[0], int(x[2:])) for x in infile.readlines()]

def count_pos(moves):
    visited = set()
    head, tail = [0, 0], [0, 0]
    dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

    for m in moves:
        dirctn, steps = m
        for step in range(steps):
            head[0] += dirs[dirctn][0]
            head[1] += dirs[dirctn][1]

            diff_x, diff_y = head[0] - tail[0], head[1] - tail[1]
            if abs(diff_x) > 1 or abs(diff_x) + abs(diff_y) > 2:
                tail[0] += 1 if diff_x > 0 else -1
            if abs(diff_y) > 1 or abs(diff_x) + abs(diff_y) > 2:
                tail[1] += 1 if diff_y > 0 else -1
            visited.add(tuple(tail))

    print(len(visited))

def main():
    print(count_pos(load_data()))

if __name__ == '__main__':
    main()
