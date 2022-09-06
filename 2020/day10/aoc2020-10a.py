# AoC 2020 Day 10a

def load_data():
    with open('input.txt', 'r') as infile:
        return set([int(x) for x in infile.read().splitlines()])

def find_diffs(indata):
    curr = 0
    diffs = {1:0, 3:0}

    while True:
        for step in [1, 3]:
            if curr + step in indata:
                diffs[step] += 1
                curr += step
                break
        else:
            diffs[3] += 1
            return diffs[1] * diffs[3]

def main():
    print(find_diffs(load_data()))

if __name__ == '__main__':
    main()
