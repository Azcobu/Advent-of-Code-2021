# AoC 2015 - Day 13a
import parse
import itertools

def load_data():
    prefs = {}
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]

    for x in data:
        name, mode, amount, target = parse.parse('{} would {} {} happiness units by sitting next to {}.', x)
        if name not in prefs: prefs[name] = {}
        score = int(amount) if mode == 'gain' else int(amount) * -1
        prefs[name][target] = score
    return prefs

def calc_optimal(prefs):
    scores = {}
    for plan in itertools.permutations(prefs.keys()):
        for currpos, person in enumerate(plan):
            left_n = plan[-1] if currpos == 0 else plan[currpos-1]
            right_n = plan[currpos+1] if currpos < len(plan) - 1 else plan[0]
            scores[plan] = scores.get(plan, 0) + prefs[person][left_n] + prefs[person][right_n]
    best = sorted(scores.items(), key=lambda x:x[1], reverse = True)
    return best[0]

def main():
    data = load_data()
    print(calc_optimal(data))

if __name__ == '__main__':
    main()
