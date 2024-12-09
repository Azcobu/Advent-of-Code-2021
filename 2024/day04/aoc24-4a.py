# AoC 24 - Day 4a

def load_data() -> dict:
    letters = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, letter in enumerate(row):
                letters[(colnum, rownum)] = letter
    return letters

def main():
    found = 0
    directions = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1))

    letters = load_data()
    for pos, letter in letters.items():
        if letter == 'X':
            for d in directions:
                for num, target in enumerate(['M', 'A', 'S']):
                    check_x = d[0] * (num + 1) + pos[0]
                    check_y = d[1] * (num + 1) + pos[1]
                    if (check_x, check_y) not in letters or letters[(check_x, check_y)] != target:
                        break
                else:
                    found += 1
    print(found)

if __name__ == '__main__':
    main()
