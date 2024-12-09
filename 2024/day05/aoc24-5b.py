# AoC 24 - Day 5b

def load_data():
    with open('input.txt', 'r', encoding='utf-8') as infile:
        r, u = infile.read().split('\n\n')
    rules = [tuple(map(int, x.split('|'))) for x in r.splitlines()]
    updates = [list(map(int, x.split(','))) for x in u.splitlines()]
    return rules, updates

def is_valid(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

def main():
    rules, updates = load_data()
    middles = 0

    for update in updates:
        if not is_valid(rules, update):
            while not is_valid(rules, update):
                for r in [x for x in rules if x[0] in update and x[1] in update]:
                    r1, r2 = update.index(r[0]), update.index(r[1])
                    if r1 > r2:
                        update[r1], update[r2] = update[r2], update[r1]
            middles += update[len(update)//2]

    print(middles)

if __name__ == '__main__':
    main()
    