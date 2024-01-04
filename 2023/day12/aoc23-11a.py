# AoC 23 11a

def load_data():
    data = []
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for line in infile.readlines():
            a, b = line.split()
            data.append((a, [int(x) for x in b.split(',')]))
    return data

def validate(row, groups):
    if not row:
        return len(groups) == 0 
    if not groups:
        return '#' not in row

    if row[0] == '.':
        return validate(row[1:], groups)
    elif row[0] == '#':
        if len(row) >= groups[0] and '.' not in row[:groups[0]]:
            if len(row) == groups[0] or row[groups[0]] != '#':
                return validate(row[groups[0]+1:], groups[1:])
            return 0
        return 0
    elif row[0] == '?':
        return validate('.' + row[1:], groups) + validate('#' + row[1:], groups)

def main():
    print(sum(validate(*d) for d in load_data()))

if __name__ == '__main__':
    main()
