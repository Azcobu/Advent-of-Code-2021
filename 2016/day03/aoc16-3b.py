
def load_data():
    outdata = []
    curr1, curr2, curr3 = [], [], []
    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            t1, t2, t3 = line.split()
            curr1.append(int(t1))
            curr2.append(int(t2))
            curr3.append(int(t3))
            if len(curr1) == 3:
                outdata += curr1, curr2, curr3
                curr1, curr2, curr3 = [], [], []
    return outdata

def verify_tris(inlist):
    return sum([1 for t in inlist if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]])

def main():
    data = load_data()
    print(verify_tris(data))

if __name__ == '__main__':
    main()
