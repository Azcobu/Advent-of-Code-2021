# AoC 2023 Day 8a

def load_data():
    nodes = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        data = infile.readlines()
    path = data[0].strip()
    for line in data[2:]:
        n, _, m = line.partition(' = ')
        nodes[n] = (m[1:4], m[6:9])
    return path, nodes

def main():
    steps = 0
    curr = 'AAA'
    path, nodes = load_data()

    while curr != 'ZZZ':
        for p in path:
            curr = nodes[curr][0] if p == 'L' else nodes[curr][1]
            steps += 1
    print(steps)

if __name__ == '__main__':
    main()
