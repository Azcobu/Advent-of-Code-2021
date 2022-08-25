
def load_data():
    passports = []
    with open('input.txt', 'r') as infile:
        data = infile.read().split('\n\n')
        data = [x.replace('\n', ' ').split() for x in data]
        for person in data:
            passports.append(dict(fields.split(':') for fields in person))
    return passports

def count_valid(data):
    valid = 0
    rules = {'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
             'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
             'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
             'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or
                              (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
             'hcl': lambda x: x[0] == '#' and sum([1 for c in x[1:] if c in list('0123456789abcdef')]) == 6,
             'ecl': lambda x: x in 'amb blu brn gry grn hzl oth'.split(' '),
             'pid': lambda x: sum([1 for c in x if c.isdigit()]) == 9,
             'cid': lambda x: True}

    for p in data:
        if sum([1 for k in 'byr iyr eyr hgt hcl ecl pid'.split() if k in p and rules[k](p[k])]) >= 7:
            valid += 1
    return valid

def main():
    d = load_data()
    print(count_valid(d))

if __name__ == "__main__":
    main()