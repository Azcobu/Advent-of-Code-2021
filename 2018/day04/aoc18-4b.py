# AoC 2018 Day 4a
from parse import parse

def load_data():
    guards = {}
    times = {}
    with open('input.txt', 'r') as infile:
        d = [x.strip() for x in infile.readlines()]
        for line in sorted(d):
            chunks = line.split()
            if 'begins shift' in line:
                guardnum = int(chunks[3][1:])
                if guardnum not in times:
                    times[guardnum] = {min:0 for min in range(0, 60)}
            elif 'falls asleep' in line:
                sleep = int(chunks[1][3:-1])
            elif 'wakes up' in line:
                wake = int(chunks[1][3:-1])
                guards[guardnum] = guards.get(guardnum, 0) + (wake - sleep)
                for minute in range(sleep, wake):
                    times[guardnum][minute] += 1
    return guards, times

def find_sleep(indata):
    guards, times = indata
    maxsleep, guardnum, minnum = 0, 0, 0
    for guard, mins in times.items():
        minute, mincount = sorted(mins.items(), key=lambda x:x[1])[-1]
        if mincount > maxsleep:
                maxsleep = mincount
                guardnum = guard
                minnum = minute
    return guardnum * minnum

def main():
    print(find_sleep(load_data()))

if __name__ == '__main__':
    main()
