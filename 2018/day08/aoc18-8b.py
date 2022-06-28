def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.read().split()
    return [int(x) for x in d]

def parse(data):
    total = 0

    numkids = data.pop(0)
    nummeta = data.pop(0)

    if numkids > 0:
        children = []

        for c in range(numkids):
            children.append(parse(data))

        for m in range(nummeta):
            meta = data.pop(0)
            if meta != 0 and meta - 1 < len(children):
                total += children[meta-1]
    else:
        for m in range(nummeta):
            total += data.pop(0)

    return total

def main():
    d = load_data()
    print(parse(d))

if __name__ == '__main__':
    main()



