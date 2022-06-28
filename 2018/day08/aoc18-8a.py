def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.read().split()
    return [int(x) for x in d]

def parse(data, total):
    numkids = data.pop(0)
    nummeta = data.pop(0)

    for c in range(numkids):
        total += parse(data, 0)

    for m in range(nummeta):
        total += data.pop(0)

    return total

def main():
    print(parse(load_data(), 0))

if __name__ == '__main__':
    main()



