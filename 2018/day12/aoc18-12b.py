def load_data():
    rules = {}
    with open('input.txt', 'r') as infile:
        d = [l.strip() for l in infile.readlines()][2:]
    for x in d:
        rule, _, res = x.partition(' => ')
        rules[rule] = res
    return rules

def count_pots(state, generations, rules):

    state = [i for i, c in enumerate(state) if c == "#"]

    for tick in range(generations):
        high, low = max(state), min(state)
        statestr = ''.join('#' if pos in state else '.' for pos in range(low-4, high+5))
        maxsize = high - low + 7
        state = []
        for i in range(2, maxsize):
            currstr = statestr[i-2:i+3]
            if currstr in rules and rules[currstr] == '#':
                state.append(i - 4 + low)
    return sum(state)

def main():
    rules = load_data()
    #start = '#..#.#..##......###...###'
    start = '#...#..##.......####.#..###..#.##..########.#.#...#.#...###.#..###.###.#.#..#...#.#..##..#######.##'
    score199 = count_pots(start, 199, rules)
    score200 = count_pots(start, 200, rules)
    step_increase = score200 - score199
    print('Part 2:', count_pots(start, 200, rules) + ((50000000000 - 200) * step_increase))

if __name__ == '__main__':
    main()
