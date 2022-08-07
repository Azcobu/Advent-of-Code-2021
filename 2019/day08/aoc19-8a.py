# AoC 2019 Day 8a

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().strip()

def layer_digits(indata, width, height):
    size = width * height
    layers = [indata[i:i+size] for i in range(0, len(indata), size)]
    zeroes = {k:v.count('0') for k, v in enumerate(layers)}
    lowest = sorted(zeroes.items(), key=lambda x: x[1])[0][0]
    return layers[lowest].count('1') * layers[lowest].count('2')

def main():
    width, height = 25, 6
    print(layer_digits(load_data(), width, height))

if __name__ == '__main__':
    main()
