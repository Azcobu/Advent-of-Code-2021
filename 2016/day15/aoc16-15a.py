# AoC 2016 - Day 15
import parse

def load_data():
    out = {}
    with open('input.txt', 'r') as infile:
        indata = [x.strip() for x in infile.readlines()]
    for x in indata:
        disc, numpos, currpos = parse.parse('Disc #{} has {} positions; at time=0, it is at position {}.', x)
        out[int(disc)] = int(numpos), int(currpos)
    return out

def find_time(state):
    time = 0
    while True:
        for k, v in state.items():
            if (state[k][1] + time + k) % state[k][0] != 0:
                break
        else:
            return time
        time += 1

def main():
    test = {1: (5, 4), 2: (2, 1)}
    assert find_time(test) == 5
    print(find_time(load_data()))

if __name__ == '__main__':
    main()
