# AoC 24 - Day 5a

def load_data():
    with open('input.txt', 'r', encoding='utf-8') as infile:
        r, u = infile.read().split('\n\n')
    rules = [tuple(map(int, x.split('|'))) for x in r.splitlines()]
    updates = [list(map(int, x.split(','))) for x in u.splitlines()]
    return rules, updates

def main():
    rules, updates = load_data()
    middles = 0

    for update in updates:
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    break
        else:
            middles += update[len(update)//2]

    print(middles)

if __name__ == '__main__':
    main()
    