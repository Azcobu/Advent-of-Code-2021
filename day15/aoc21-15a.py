cmap = r'aoc21-15-input.txt'

def get_data(cmap):
    with open(cmap, 'r') as infile:
        indata = infile.read()

    maplist = []
    for line in indata.splitlines():
        maplist.append([int(x) for x in list(line)])
    return maplist

def findpath(startnode, riskmap, path=[]):
    endnode = len(riskmap) - 1, len(riskmap[0]) - 1
    if startnode == endnode:
        if sum(path) < findpath.minpath:
            findpath.minpath = sum(path)
            print(f'Path risk reduced to {findpath.minpath}')
        yield path
    else:
        if sum(path) < findpath.minpath:
            if startnode[1] < len(riskmap[0]) - 1: # go right
                riskval = riskmap[startnode[0]][startnode[1] + 1]
                yield from findpath((startnode[0], startnode[1] + 1), riskmap, path + [riskval])
            if startnode[0] < len(riskmap) - 1: # go down
                riskval = riskmap[startnode[0] + 1][startnode[1]]
                yield from findpath((startnode[0] + 1, startnode[1]), riskmap, path + [riskval])

def main():
    findpath.minpath = 999999
    riskmap = get_data(cmap)
    paths = [sum(x) for x in findpath((0, 0), riskmap)]
    print(min(paths))

if __name__ == '__main__':
    main()
