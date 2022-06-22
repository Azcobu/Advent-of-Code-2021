# AoC 2018 - Day 7a
from collections import defaultdict

def load_data():
    prereqs = defaultdict(list)
    with open('input.txt', 'r') as infile:
        for line in infile.read().splitlines():
            words = line.split()
            prereqs[words[7]].append(words[1])
            for s in words[1], words[7]:
                if s not in prereqs:
                    prereqs[s] = []
    print(prereqs)
    return prereqs

def order_steps(prereqs):
    done = []

    while True:
        available = []
        for k, v in prereqs.items():
            if all([True if x in done else False for x in v]) and k not in done:
                available.append(k)
        if available:
            done.append(sorted(available)[0])
        else:
            return ''.join(done)

def main():
    print(order_steps(load_data()))

if __name__ == '__main__':
    main()
