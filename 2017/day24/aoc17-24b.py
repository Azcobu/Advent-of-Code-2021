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
    bridges = list(find_bridges(load_data(), [0]))
    max_len = max(len(x) for x in bridges)
    print(max(sum(x) for x in bridges if len(x) == max_len))

if __name__ == '__main__':
    main()
