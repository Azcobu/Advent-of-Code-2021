from knothash import knothash

def calc_used(key):
    total = 0
    for row in range(128):
        k = knothash(f'{key}-{row}')
        b = bin(int(k, 16))[2:].zfill(128)
        total += b.count('1')
    return total

def main():
    assert calc_used('flqrgnkx') == 8108
    print(calc_used('ljoxqyyw'))

if __name__ == '__main__':
    main()
