from parse import parse

def load_data():
    probes = {}
    parsestr = 'pos=<{},{},{}>, r={}'
    with open('input.txt', 'r') as infile:
        for num, line in enumerate([x.strip() for x in infile.readlines()]):
            x, y, z, rad = [int(x) for x in parse(parsestr, line)]
            probes[num] = (x, y, z, rad)
    return probes

def find_in_rad(probes):
    count = 0
    bigprobe, bigcoords = sorted(probes.items(), key=lambda x:x[1][3])[-1]
    
    for k, v in probes.items():
        dist = sum([abs(bigcoords[x] - v[x]) for x in range(3)])
        if dist <= bigcoords[3]:
            count += 1
    return count

def main():
    data = load_data()
    print(find_in_rad(data))

if __name__ == '__main__':
    main()
