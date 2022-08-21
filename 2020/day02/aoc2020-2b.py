from parse import parse

def load_data():
    rules = []
    parsestr = '{}-{} {}: {}'
    with open('input.txt', 'r') as infile:
        for line in [x.strip() for x in infile.readlines()]:
            minl, maxl, lett, passwd = parse(parsestr, line)
            rules.append((int(minl), int(maxl), lett, passwd))
    return rules

def count_valid(rules):
    return sum(1 for r in rules if (r[3][r[0] - 1] == r[2]) ^ (r[3][r[1] - 1] == r[2]))

def main():
    print(count_valid(load_data()))

if __name__ == '__main__':
    main()
