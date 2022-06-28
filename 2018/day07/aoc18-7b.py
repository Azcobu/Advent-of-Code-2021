# AoC 2018 - Day 7b
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
    return prereqs

    return ord(letter) - 4

def track_time(prereqs):
    numworkers = 5
    tick = 0
    workers, working, done = [], [], []

    while len(done) < len(prereqs.keys()):
        new = []
        for x in workers:
            if x[1] > 1:
                new.append((x[0], x[1]-1))
            else:
                done.append(x[0])
        workers = new

        while len(workers) < numworkers:
            available = []
            for k, v in prereqs.items():
                if all([True if x in done else False for x in v]) and k not in working:
                    available.append(k)
            if available:
                nextlett = sorted(available)[0]
                workers.append((nextlett, ord(nextlett)-4))
                working.append(nextlett)
            else:
                break
        tick += 1

    return tick-1

def main():
    print(track_time(load_data()))

if __name__ == '__main__':
    main()
