# AoC 2022 Day 3a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def find_priorities(sacks):
    total = 0
    for g in range(len(sacks) // 3):
        uniq = list(set(sacks[g*3]) & set(sacks[g*3 + 1]) & set(sacks[g*3 + 2]))[0]
        total += ord(uniq) - 96 if uniq.islower() else ord(uniq) - 38
    return total
        
def main():
    print(find_priorities(load_data()))

if __name__ == '__main__':
    main()
