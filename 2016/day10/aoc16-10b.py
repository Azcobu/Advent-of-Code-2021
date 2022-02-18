# AoC 2016 - Day 10b
from parse import *
from collections import defaultdict
from math import prod

def load_data():
    instrs = []
    with open('input.txt', 'r') as infile:
        indata = [x.strip() for x in infile.readlines()]

    for line in indata:
        if 'value' in line: # value 2 goes to bot 143
            val, bot = search('value {:d} goes to bot {:d}', line)
            instrs.append([val, bot])
        else: # bot 115 gives low to output 2 and high to bot 80
            source, lowtarg, lowval, hightarg, highval =\
            search('bot {:d} gives low to {} {:d} and high to {} {:d}', line)
            instrs.append([source, lowtarg, lowval, hightarg, highval])
    return instrs

def parse(instrs):
    bots, output = defaultdict(list), defaultdict(list)
    types = {'bot':bots, 'output':output}
    done = []

    while len(instrs) > len(done):
        for i in instrs:
            if i not in done:
                if len(i) == 2:
                    bots[i[1]].append(i[0])
                    done.append(i)
                else:
                    if len(bots[i[0]]) == 2:
                        val1, val2 = sorted(bots[i[0]])
                        types[i[1]][i[2]].append(val1)
                        types[i[3]][i[4]].append(val2)
                        done.append(i)
    print(prod([output[x][0] for x in range(3)]))

def main():
    d = load_data()
    parse(d)

if __name__ == '__main__':
    main()
