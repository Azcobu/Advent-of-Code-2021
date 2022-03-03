# AoC 2017 - Day 1a

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().strip()

def find_sum(instr):
    return sum([int(c) if c == instr[(pos + 1) % len(instr)] else 0 for pos, c in enumerate(instr)])

def main():
    print(find_sum(load_data()))

if __name__ == '__main__':
    main()
