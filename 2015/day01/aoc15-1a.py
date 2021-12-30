# AoC 2015 - 1a

def load_data(infile):
    with open(infile, 'r') as indata:
        data = indata.read()
    return data.strip()

def find_floor(indata):
    return indata.count('(') - indata.count(')')

def main():
    data = load_data('input.txt')
    print(find_floor(data))

if __name__ == '__main__':
    main()
