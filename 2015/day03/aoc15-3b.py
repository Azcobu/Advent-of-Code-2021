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
    return set(visited)

def stream_manage(dirstream):
    s1 = track_deliveries(dirstream[::2])
    s2 = track_deliveries(dirstream[1::2])
    return len(s1 | s2)

def main():
    assert stream_manage('^v') == 3
    assert stream_manage('^>v<') == 3
    assert stream_manage('^v^v^v^v^v') == 11
    path = load_data()
    print(stream_manage(path))

if __name__ == '__main__':
    main()
