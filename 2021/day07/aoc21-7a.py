# Adventof Code 2021 - 7a

indata = '16,1,2,0,4,2,7,1,2,14'
indata = [int(x) for x in indata.split(',')]

def load_data():
    with open(r'D:\Python\Code\aoc21\aoc-7-input.txt', 'r') as infile:
        indata = infile.readline()
    return [int(x) for x in indata.split(',')]

def calc_min_fuel(indata):
    results = {}
    for pos in range(max(indata)):
        for c in indata:
            results[pos] = results.get(pos, 0) + abs(pos - c)
    return min(x for x in results.values())

def main():
    indata = load_data()
    print(calc_min_fuel(indata))

if __name__ == '__main__':
    main()
