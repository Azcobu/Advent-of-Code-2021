paths = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

def load_data(infile):
    cavemap = {}
    for line in paths.splitlines():
        start, null, dest = line.partition('-')
        cavemap[start] = cavemap.get(start, []) + [dest]
        cavemap[dest] = cavemap.get(dest, []) + [start]
    return cavemap

def find_paths(cavemap, currpath, double, doublecount):
    currpos = currpath[-1]
    if currpos == 'end':
        yield currpath
    else:
        for poss in cavemap[currpos]:
            if poss.islower() and poss in currpath:
                if poss == double and doublecount == 2:
                    doublecount = 1
                    yield from find_paths(cavemap, currpath + [poss], double, 1)
            else:
                yield from find_paths(cavemap, currpath + [poss], double, doublecount)

def main():
    cavemap = load_data(paths)
    lowers = [x for x in cavemap.keys() if x.islower() and x not in ['start', 'end']]
    pathcount = 0
    for l in lowers:
        for x in find_paths(cavemap, ['start'], l, 2):
            print(x)
            pathcount += 1
    print(pathcount)

if __name__ == '__main__':
    main()
