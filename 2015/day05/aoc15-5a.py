# AoC 2015 - Day 5

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def check_vowels(instr):
    return sum([1 for x in instr if x in ['a', 'e', 'i', 'o', 'u']]) >= 3

def check_twicerow(instr):
    for x in set(instr):
        if x + x in instr:
            return True
    return False

def check_forbidden(instr):
    for x in ['ab', 'cd', 'pq', 'xy']:
        if x in instr:
            return True
    return False

def checker(instr):
    return not check_forbidden(instr) and check_vowels(instr) and check_twicerow(instr)

def main():
    print(checker('ugknbfddgicrmopn'))
    print(checker('aaa'))
    print(checker('jchzalrnumimnmhp'))
    print(checker('haegwjzuvuyypxyu'))
    print(checker('dvszwmarrgswjxmb'))
    indata = load_data()
    print(sum([1 for x in indata if checker(x)]))

if __name__ == '__main__':
    main()
