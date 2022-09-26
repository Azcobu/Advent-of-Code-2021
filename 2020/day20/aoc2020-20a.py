# AoC 2020 Day 20a

def load_data():
    tiles = {}
    with open('input.txt', 'r') as infile:
        d = infile.read()
    for t in d.split('\n\n'):
        tile = t.split('\n')
        tilename = tile[0][5:-1]
        tilesize = len(tile[1])
        top = tile[1]
        bottom = tile[tilesize]
        left = ''.join([x[0] for x in tile[1:]])
        right = ''.join([x[tilesize-1] for x in tile[1:]])
        tiles[tilename] = [top, right, bottom, left]
    return tiles

def find_match(tiles, curr_tile, side):
    for tile, sides in tiles.items():
        if tile != curr_tile:
            for s in sides:
                if s == side or s[::-1] == side:
                    return True
    return False 

def find_corners(tiles):
    corner_ids = 1
    sidematches = {x: 0 for x in tiles.keys()}

    for curr_tile, sides in tiles.items():
        for side in sides:
            if find_match(tiles, curr_tile, side):
                sidematches[curr_tile] += 1
    
    for k, v in sidematches.items():
        if v == 2:
            corner_ids *= int(k)
    return corner_ids

def main():
    print(find_corners(load_data()))

if __name__ == '__main__':
    main()
