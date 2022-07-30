# AoC 2019 Day 4a

def has_adjacent(innum):
    return any([True for x in range(10) if str(x)*2 in str(innum)])

def never_decrease(innum):
    return list(str(innum)) == sorted(str(innum))

def count_valid(start, end):
    return sum([1 for x in range(start, end+1) if has_adjacent(x) and never_decrease(x)])

def main():
    print(count_valid(357253, 892942))

if __name__ == '__main__':
    main()
