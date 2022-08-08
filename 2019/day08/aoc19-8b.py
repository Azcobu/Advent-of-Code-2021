# AoC 2019 Day 8a

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().strip()

def decode(indata, width, height):
    size = width * height
    layers = [indata[i:i+size] for i in range(0, len(indata), size)]
    for h in range(height):
        for w in range(width):
            for l in layers:
                char = l[h*width+w]
                if char != '2':
                    break
            print(f'{"#" if char == "1" else " "}', end='')
        print()

def main():
    width, height = 25, 6
    print(decode(load_data(), width, height))

if __name__ == '__main__':
    main()
