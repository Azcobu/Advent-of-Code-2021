# AoC 2019 Day 6a

def load_data():
    objlist = {}

    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            p, m = [x.strip() for x in line.split(')')]
            objlist[p] = objlist.get(p, [])
            objlist[m] = objlist.get(m, []) + [p]
    return objlist

def sum_orbits(object, data):
    return 0 if data[object] == [] else sum([1 + sum_orbits(x, data) for x in data[object]])

def sum_all(data):
    return sum([sum_orbits(obj, data) for obj in data.keys()])

def main():
    print(sum_all(load_data()))

if __name__ == '__main__':
    main()
