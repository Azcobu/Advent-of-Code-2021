
def load_data():
    data = {}
    with open('input.txt', 'r') as infile:
        d = [l.strip() for l in infile.readlines()][2:]
    for x in d:
        rule, _, res = x.partition(' => ')
        data[rule] = res

    data = {'...##' : '#', 
            '..#..' : '#', 
            '.#...' : '#',
            '.#.#.' : '#',
            '.#.##' : '#',
            '.##..' : '#',
            '.####' : '#',
            '#.#.#' : '#',
            '#.###' : '#',
            '##.#.' : '#',
            '##.##' : '#',
            '###..' : '#',
            '###.#' : '#',
            '####.' : '#'}
    return data

def count_pots(start, generations, rules):
    
    state = '....' + start + '....'
    for tick in range(generations):
        newstr = list(state)
        changes = {}
        for k, v in rules.items():
            while k in state:
                pos = state.index(k)
                changes[pos+2] = v

        for k, v in changes.items():
            newstr[k] = v
        state = ''.join(newstr)

def main():
    rules = load_data()
    print(rules)
    start = '#..#.#..##......###...###'
    print(count_pots(start, 20, rules))

if __name__ == '__main__':
    main()
