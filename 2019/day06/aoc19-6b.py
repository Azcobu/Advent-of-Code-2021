# AoC 2019 Day 6b

def load_data():
    objlist = {}

    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            prim, moon = [x.strip() for x in line.split(')')]
            objlist[prim] = objlist.get(prim, []) + [moon]
            objlist[moon] = objlist.get(moon, [])
    return objlist

def return_path(data, current, target, path):
    if target in data[current]:
        yield path
    else:
        for moon in data[current]:
            yield from return_path(data, moon, target, path + [moon])

def find_transfers(data):
    youpath = list(return_path(data, 'COM', 'YOU', ['COM']))[0]
    sanpath = list(return_path(data, 'COM', 'SAN', ['COM']))[0]
    for step, diff in enumerate(zip(youpath, sanpath)):
        if diff[0] != diff[1]:
            break
    return len(youpath) + len(sanpath) - (2 * step)

def main():
    print(find_transfers(load_data()))

if __name__ == '__main__':
    main()
