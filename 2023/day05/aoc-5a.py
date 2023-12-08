# AoC 2023 Day 5a
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

def main():
    lowest = 9999999999999
    seeds, maps = load_data()
    for s in seeds:
        for m in maps:
            for rule in m:
                if rule[1] <= s < rule[1] + rule[2]:
                    s -= rule[1] - rule[0]
                    break
        if s < lowest:
            lowest = s
    print(lowest)

if __name__ == '__main__':
    main()
