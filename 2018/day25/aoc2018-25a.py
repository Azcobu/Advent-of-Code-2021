# AoC 2018 Day 25a

def load_data():
    vals = []
    with open('input.txt', 'r') as infile:
        for line in infile.read().splitlines():
            x, y, z, k = map(int, line.split(','))
            vals.append((x, y, z, k))
    return vals

def count_consts(points):
    consts = []

    for p in points:
        p_near = set()
        for q in points:
            if sum(abs(p[x] - q[x]) for x in range(4)) <= 3:
                p_near.add(q)
        consts.append(p_near)

    for k in range(2):
        unique = []
        for s in consts:
            for t in consts:
                if s != t:
                    if not s.isdisjoint(t):
                        s |= t
            if s not in unique:
                unique.append(s)
        consts = unique     
    print(len(consts))

def main():
    count_consts(load_data())

if __name__ == '__main__':
    main()
