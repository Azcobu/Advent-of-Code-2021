# AoC 2016 - Day 18b

def calc_row(inrow):
    newrow = []
    inrow = f'.{inrow}.'
    for pos in range(1, len(inrow)-1):
        seq = inrow[pos-1:pos+2]
        if seq in ['^^.', '.^^', '^..', '..^']:
            newrow.append('^')
        else:
            newrow.append('.')
    return ''.join(newrow)

def count_safe(rowcount, start):
    rows = [start.count('.')]
    for c in range(rowcount-1):
        start = calc_row(start)
        rows.append(start.count('.'))
    return sum(rows)

def main():
    start = '^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^' +\
            '.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.'
    assert count_safe(10, '.^^.^.^^^^') == 38
    print(count_safe(400000, start))

if __name__ == '__main__':
    main()
