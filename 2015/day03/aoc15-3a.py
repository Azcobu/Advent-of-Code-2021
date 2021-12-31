# AOC 2015 - Day 3

def load_data():
    with open('input.txt', 'r') as infile:
        indata = infile.read()
    return indata.strip()

def track_deliveries(dirstream):
    currpos = (0, 0)
    visited = [currpos]
    moves = {'>':(1, 0), '<':(-1, 0), '^':(0, 1), 'v':(0, -1)}

    for instruct in dirstream:
        shift = moves[instruct]
        currpos = currpos[0] + shift[0], currpos[1] + shift[1]
        visited.append(currpos)
    return len(set(visited))

def main():
    assert track_deliveries('^>v<') == 4
    assert track_deliveries('^v^v^v^v^v') == 2
    path = load_data()
    print(track_deliveries(path))

if __name__ == '__main__':
    main()
