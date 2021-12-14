paths = '''xx-xh
vx-qc
cu-wf
ny-LO
cu-DR
start-xx
LO-vx
cu-LO
xx-cu
cu-ny
xh-start
qc-DR
vx-AP
end-LO
ny-DR
vx-end
DR-xx
start-DR
end-ny
ny-xx
xh-DR
cu-xh
'''

def load_data(infile):
    cavemap = {}
    for line in paths.splitlines():
        start, null, dest = line.partition('-')
        cavemap[start] = cavemap.get(start, []) + [dest]
        if start != 'start':
            cavemap[dest] = cavemap.get(dest, []) + [start]
    return cavemap

def find_paths(cavemap, currpath, double):
    if currpath == ['start', 'A', 'b', 'A', 'b', 'A'] and double == 'b':
        print('vfd')
    currpos = currpath[-1]
    if currpos == 'end':
        yield currpath
    else:
        for poss in cavemap[currpos]:
            if poss.islower() and poss in currpath:
                if poss == double and currpath.count(double) <= 1:
                    yield from find_paths(cavemap, currpath + [poss], double)
            else:
                yield from find_paths(cavemap, currpath + [poss], double)

def main():
    cavemap = load_data(paths)
    lowers = [x for x in cavemap.keys() if x.islower() and x not in ['start', 'end']]
    pathlist = []
    for l in lowers:
        for x in find_paths(cavemap, ['start'], l):
            pathlist.append(','.join(x))
            #print(','.join(x))
    print(len(list(set(pathlist))))

if __name__ == '__main__':
    main()
