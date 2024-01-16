# AoC 2023 Day 15a

def load_data():
    with open('input.txt', 'r', encoding='utf-8') as infile:
        return infile.read()

def hashstr(instr):
    val = 0
    for c in instr:
        val = ((val + ord(c)) * 17) % 256
    return val

def main():
    print(sum([hashstr(s) for s in load_data().split(',')]))

if __name__ == '__main__':
    main()
