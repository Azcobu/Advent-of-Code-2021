def load_data():
    with open('input.txt', 'r') as infile:
        return list(map(int, infile.read().split(","))) 

def run_code(intcode, val1, val2):
    pos = 0
    intcode[1] = val1
    intcode[2] = val2

    while True:
        op = intcode[pos]
        if op == 99:
            break
        else:
            a, b, c = intcode[pos+1], intcode[pos+2], intcode[pos+3]
            if op == 1:
                intcode[c] = intcode[a] + intcode[b]
            elif op == 2:
                intcode[c] = intcode[a] * intcode[b]
        pos += 4
    return intcode[0]

def search(intcode, target):
    for noun in range(100):
        for verb in range(100):
            if run_code(intcode.copy(), noun, verb) == target:
                return f'{noun}{verb}'

def main():
    intcode = load_data()
    print(search(intcode, 19690720))

if __name__ == '__main__':
    main()
