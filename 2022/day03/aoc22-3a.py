# AoC 2022 Day 3a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def find_priorities(sacks):
    total = 0
    for s in sacks:
        mid = len(s) // 2
        uniq = [x for x in s[:mid] if x in s[mid:]][0]
        total += ord(uniq) - 96 if uniq.islower() else ord(uniq) - 38
    return total
        
def main():
    print(find_priorities(load_data()))

if __name__ == '__main__':
    main()
