#AoC 2017 - Day 24a
import copy

def load_data():
    comps = set()
    with open('input.txt', 'r') as infile:
        for line in infile.read().splitlines():
            a, b = line.split('/')
            comps.add((int(a), int(b)))
    return comps

def find_bridges(comps, bridge):
    matches = [x for x in comps if x[0] == bridge[-1] or x[1] == bridge[-1]]
    if not matches:
        yield bridge
    else:
        for m in matches:
            newset = copy.copy(comps)
            newset.remove(m)
            newcomp = [m[0], m[1]] if m[0] == bridge[-1] else [m[1], m[0]]
            yield from find_bridges(newset, bridge + newcomp)

def main():
    comps = load_data()
    #comps = set([(0, 2), (2, 2), (2, 3), (3, 4), (3, 5), (0, 1), (10, 1), (9, 10)])
    print(max(sum(x) for x in find_bridges(comps, [0])))

if __name__ == '__main__':
    main()
