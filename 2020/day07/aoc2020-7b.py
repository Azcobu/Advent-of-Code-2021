
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
    return 1 + sum([bags[target][b] * count_children(bags, b) for b in bags[target]])

def main():
    print(count_children(load_data(), 'shiny gold') - 1)

if __name__ == '__main__':
    main()
