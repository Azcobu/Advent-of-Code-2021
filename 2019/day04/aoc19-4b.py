# AoC 2019 Day 4b

def has_2adjacent(innum):
    for x in set(str(innum)):
        if str(innum).count(x) == 2:
            return True
    return False

def never_decrease(innum):
    return list(str(innum)) == sorted(str(innum))

def count_valid(start, end):
    return sum([1 for x in range(start, end+1) if never_decrease(x) and has_2adjacent(x)])

def main():
    print(count_valid(357253, 892942))

if __name__ == '__main__':
    main()
