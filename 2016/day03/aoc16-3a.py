
def load_data():
    with open('input.txt', 'r') as infile:
        return [[int(y) for y in x.split()] for x in infile.readlines()]

def verify_tris(inlist):
    valid = 0
    return sum([1 for t in inlist if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]])

def main():
    print(verify_tris(load_data()))

if __name__ == '__main__':
    main()
