# AoC 2015 - 1a

def load_data(infile):
    with open(infile, 'r') as indata:
        data = indata.read()
    return data.strip()

def find_basepos(indata):
    currfloor = 0
    for pos, char in enumerate(indata):
        if char == '(':
            currfloor += 1
        elif char == ')':
            currfloor -= 1
        if currfloor == -1:
            return pos + 1

def main():
    data = load_data('input.txt')
    print(find_basepos(data))

if __name__ == '__main__':
    main()
