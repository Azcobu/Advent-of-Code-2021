# AoC 2015 - Day 25a

def find_target(targ_row, targ_col):
    row, col = 1, 1
    code = 20151125

    while True:
        if row == 1:
            row = col + 1
            col = 1
        else:
            row -= 1
            col += 1

        code = (code * 252533) % 33554393

        if row == targ_row and col == targ_col:
            return code

def main():
    print(find_target(2981, 3075))

if __name__ == '__main__':
    main()
