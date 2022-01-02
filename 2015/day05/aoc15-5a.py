# AoC 2015 - Day 5

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def check_vowels(instr):
    return sum([1 for x in instr if x in ['a', 'e', 'i', 'o', 'u']]) >= 3

def check_twicerow(instr):
    return sum([1 for x in set(instr) if x+x in instr]) > 0

def check_forbidden(instr):
    return any([x in instr for x in ['ab', 'cd', 'pq', 'xy']])

def checker(instr):
    return not check_forbidden(instr) and check_vowels(instr) and check_twicerow(instr)

def main():
    assert checker('ugknbfddgicrmopn') == True
    assert checker('aaa') == True
    assert checker('jchzalrnumimnmhp') == False
    assert checker('haegwjzuvuyypxyu') == False
    assert checker('dvszwmarrgswjxmb') == False
    indata = load_data()
    print(sum([1 for x in indata if checker(x)]))

if __name__ == '__main__':
    main()
