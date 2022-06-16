# AoC 2018 - Day 2a

def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.readlines()
        return [x.strip() for x in d]

def gen_checksum(data):
    count2, count3 = 0, 0

    for s in data:
        letts = set(s)
        if any([True for l in letts if s.count(l) == 2]):
            count2 += 1 
        if any([True for l in letts if s.count(l) == 3]):
            count3 += 1 
        
    return count2 * count3

def main():
    data = load_data()
    print(gen_checksum(data))

if __name__ == '__main__':
    main()
