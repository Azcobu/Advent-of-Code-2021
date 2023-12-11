# AoC 2023 Day 5b
import re

def load_data():
    maps = []
    with open('input.txt', 'r', encoding='utf-8') as infile:
        data = infile.read().split('\n\n')
    seeds = [int(x.group()) for x in re.finditer(r'\d+', data[0])]
    for mapping in data[1:]:
        newmaps = []
        for line in mapping.split('\n')[1:]:
            newmaps.append([int(x.group()) for x in re.finditer(r'\d+', line)])
        maps.append(newmaps)
    return seeds, maps

def find_loc(seed, maps):
    for m in maps:
        for rule in m:
            if rule[1] <= seed < rule[1] + rule[2]:
                seed -= rule[1] - rule[0]
                break
    return seed

def main():
    lowstep = 0
    lowlist = []
    seeds, maps = load_data()

    for s1, rng in zip(seeds[::2], seeds[1::2]):
        lowest = 9999999999999
        lowstart, lowend = s1, s1 + rng
        for exp in [5, 2, 0]:
            print(f'Downshifting to {10**exp}')
            srchrnge = [x for x in range(lowstart, lowend, 10 ** exp)] + [lowend]
            if len(srchrnge) >= 10000:
                break
            print(f'searching {len(srchrnge)} entries between {lowstart} and {lowend}.')
            for step in srchrnge:
                loc = find_loc(step, maps)
                if loc < lowest:
                    lowest = loc
                    lowstep = step
                    lowstart = max(s1, lowstep - 10 ** exp)
                    lowend = min(s1 + rng, lowstep + 10 ** exp)
                    print(f'New low - {loc} - step {exp}')
        lowlist.append(lowest)

    print(min(lowlist))

if __name__ == '__main__':
    main()
