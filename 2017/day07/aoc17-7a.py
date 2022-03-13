# AoC 2017 - Day 7a

def find_parent():
    allnames, child = set(), set()
    with open('input.txt', 'r') as infile:
        for x in infile:
            name, _, children = x.strip().partition(' -> ')
            allnames.add(name[:name.find(' (')])
            if children != '':
                child |= set([z.strip() for z in children.split(',')])
    return list(allnames - child)[0]

def main():
    print(find_parent())

if __name__ == '__main__':
    main()
