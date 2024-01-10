# AoC 2023 Day 14a

def load_data():
    rocks = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, char in enumerate(row):
                if char in '#O':
                    rocks[(colnum, rownum)] = char
    return rocks

def calc_load(rocks):
    maxrow = max([x[1] for x in rocks.keys()])
    newrocks = {}

    for coords, rock in rocks.items():
        if rock == '#':
            newrocks[coords] = '#'
        else:
            nx, ny = coords[0], coords[1]
            while (nx, ny - 1) not in newrocks and (ny - 1) >= 0:
                ny -= 1
            newrocks[(nx, ny)] = 'O'

    return sum([maxrow - coords[1] + 1 for coords, rock in newrocks.items() if rock == 'O'])

def main():
    print(calc_load(load_data()))

if __name__ == '__main__':
    main()
