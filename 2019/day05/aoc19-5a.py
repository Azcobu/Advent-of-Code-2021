def load_data():
    with open('input.txt', 'r') as infile:
        return list(map(int, infile.read().split(","))) 

def run_code(intcode, main=False):
    pos = 0

    if main:
        intcode[1] = 12
        intcode[2] = 2

    while True:
        if intcode[pos] == 99:
            break
        elif intcode[pos] == 1:
            intcode[intcode[pos+3]] = intcode[intcode[pos+1]] + intcode[intcode[pos+2]]
        elif intcode[pos] == 2:
            intcode[intcode[pos+3]] = intcode[intcode[pos+1]] * intcode[intcode[pos+2]]
        elif intcode[pos] == 3:
            pass

        elif intcode[pos] == 4:
            pass


        pos += 4
    return intcode

def main():
    assert run_code([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert run_code([2,3,0,3,99]) == [2, 3, 0, 6, 99]
    assert run_code([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert run_code([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
    intcode = load_data()
    print(run_code(intcode, True))

if __name__ == '__main__':
    main()
