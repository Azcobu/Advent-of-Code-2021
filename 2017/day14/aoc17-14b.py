from knothash import knothash

def generate_grid(key):
    coords = set()
    for y in range(128):
        k = knothash(f'{key}-{y}')
        b = bin(int(k, 16))[2:].zfill(128)
        for x, val in enumerate(b):
            if val == '1':
                coords.add((x, y))
    return coords

def calc_regions(coords):
    found = 0
    queue = set()

    while coords:
        found += 1
        queue.add(coords.pop())
        while queue:
            (x, y) = queue.pop()
            for local in [(x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if local in coords:
                    coords.remove(local)
                    queue.add(local)
    return found

def main():
    g = generate_grid('ljoxqyyw')
    print(calc_regions(g))

if __name__ == '__main__':
    main()
