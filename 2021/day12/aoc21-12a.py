paths ='''xx-xh
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
        cavemap[dest] = cavemap.get(dest, []) + [start]
    return cavemap

def find_paths(cavemap, currpath):
    currpos = currpath[-1]
    if currpos == 'end':
        yield currpath
    else:
        for poss in cavemap[currpos]:
            if poss.islower() and poss in currpath:
                pass
            else:
                yield from find_paths(cavemap, currpath + [poss])

def main():
    cavemap = load_data(paths)
    print(len([x for x in find_paths(cavemap, ['start'])]))

if __name__ == '__main__':
    main()
