# AoC 2019 - Day 14a

def load_data():
    reactions = {}
    with open('example1.txt', 'r') as infile:
        d = infile.read().splitlines()
    for line in d:
        inchem, outchem = map(parse, line.split(' => '))

        reactions[outchem[0][1]] = {outchem[0][0]: inchem}
    return reactions

def parse(ingreds):
    i = []
    for ingred in ingreds.split(', '):
        num, chem = ingred.split(' ')
        i.append([int(num), chem])
    return i

def find_amount(reactions):
    needs = {'FUEL': 1}

    while needs:
        for chem, needed in needs.items():
            amnt, ingreds = reactions[chem]
            mult = needed // amnt
            for i in ingreds:
                needs[i[1]] = needs.get(i[1], 0) + i[0] * mult

def main():
    find_amount(load_data())

if __name__ == '__main__':
    main()
