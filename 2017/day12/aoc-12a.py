# AoC 2017 - Day 12a

def load_data():
    pipes = {}
    with open('input.txt', 'r') as infile:
        for x in [k.strip() for k in infile.readlines()]:
            pipe, _, conns = x.partition(' <-> ')
            pipes[int(pipe)] = [int(y) for y in conns.split(', ')]
    return pipes

def count_connected(data, target):
    found = set()
    queue = [target]
    while queue:
        curr = queue.pop()
        for x in data[curr]:
            if x not in found:
                queue.append(x)
                found.add(x)
    return len(set(found))

def main():
    d = load_data()
    #d = {0:[2], 1:[1], 2:[0, 3, 4], 3:[2, 4], 4:[2, 3, 6], 5:[6], 6:[4, 5]}
    print(count_connected(d, 0))

if __name__ == '__main__':
    main()
