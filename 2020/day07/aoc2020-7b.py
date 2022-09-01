
def load_data():
    bags = {}
    with open('input.txt', 'r') as infile:
        d = infile.read().strip().split('\n')
    for bag in d:
        parent, contains, children = bag.partition('contain')
        parent = parent.partition('bags')[0].strip()
        if 'no other bags' in children:
            children = []
        else:
            children = children[:-1].split(',')
            children = [x.partition('bag')[0].strip() for x in children]
            children = {x[2:]:int(x[0]) for x in children}
        bags[parent] = children
    return bags

def count_children(bags, target):
    poss = bags[target]
    found = set()
    total = 0

    while poss:
        curr = poss.pop()
        found.add(curr)
        total += bags[curr]
        poss += [k for k, v in bags.items() if curr in v and k not in found and k not in poss]
    print(len(found))

def main():
    print(count_children(load_data(), 'shiny gold'))

if __name__ == '__main__':
    main()
