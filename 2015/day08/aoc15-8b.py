# AoC 2015 - Day 8

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile]

def calc_strlens(data):
    esclen, baselen, total = 0, 0, 0
    for x in data:
        esctxt = [k for k in x if k not in ['"', '\\']]
        esclen = 2 + (2 * x.count('"')) + (2 * x.count('\\')) + len(esctxt)
        baselen = len(x)
        total += esclen - baselen
        print(f'{esclen} - {baselen}')
    return total

def main():
    data = load_data()
    print(calc_strlens(data))

if __name__ == '__main__':
    main()
