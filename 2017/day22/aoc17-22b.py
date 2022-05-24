#AoC 2017 - Day 22a

def load_data():
    grid = {}
    with open('input.txt', 'r') as infile:
        for rownum, row in enumerate(infile.read().splitlines()):
            for colnum, char in enumerate(row):
                if char == '#':
                    grid[(colnum, rownum)] = 'I'
    return grid

def count_infections(grid):
    curr_dir, infs = 0, 0
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    turns = {'C': -1, 'W': 0, 'I': 1, 'F': 2}
    changes = list(turns.keys())

    x = round(max([k[0] for k in grid])/2)
    y = round(max([k[1] for k in grid])/2)

    for burst in range(10000000):

        curr_node = grid[(x, y)] if (x, y) in grid else 'C'
        turn_dir = turns[curr_node]
        curr_dir = (curr_dir + turn_dir) % 4

        node_type_idx = (changes.index(curr_node) + 1) % 4
        grid[(x, y)] = changes[node_type_idx]

        if node_type_idx == 2:
            infs += 1

        x, y = (x + moves[curr_dir][0], y + moves[curr_dir][1])

    return infs

def main():
    print(count_infections(load_data()))

if __name__ == '__main__':
    main()
