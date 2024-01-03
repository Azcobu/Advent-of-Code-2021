# AoC 23 11a

def load_data():
    data = []
    with open('example.txt', 'r', encoding='utf-8') as infile:
        for line in infile.readlines():
            a, b = line.split()
            data.append((a, [int(x) for x in b.split(',')]))
    return data

def validate(row, groups):
    if not row and not groups:
        return 1
    else:
        if row[0] == '.':
            return validate(row[1:], groups)
        elif row[0] == '#':
            if len(row) >= groups[0] and '.' not in row[:groups[0]]:
                if row[groups[0] + 1] == '.':
                    return validate(row[groups[0]:], groups[1:])
                elif row[groups[0] + 1] == '?':
                    newrow = row[:groups[0]] + '.' + row[groups[0] + 2:]
                    return validate(newrow, groups[1:])
                else:
                    return 0
            else:
                return 0
        elif row[0] == '?':
            return validate('.' + row[1:], groups) + validate('#' + row[1:], groups)

def main():
    print(validate('???.###', [1,1,3]))

if __name__ == '__main__':
    main()
