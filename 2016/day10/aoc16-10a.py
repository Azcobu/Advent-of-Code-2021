# AoC 2016 - Day 10a
from parse import *

def load_data():
    instrs = []
    with open('input.txt', 'r') as infile:
        indata = [x.strip() for x in infile.readlines()]
    for line in indata:
        if 'value' in line: # value 2 goes to bot 143
            val, bot = parse('value {:d} goes to bot {:d}', line)
            instrs.append([val, bot])
        else: # bot 115 gives low to output 2 and high to bot 80
            source, lowtarg, lowval, hightarg, highval =\
            parse('bot {:d} gives low to {} {:d} and high to {} {:d}', line)
            instrs.append([source, lowtarg, lowval, hightarg, highval])
    return instrs

def parse(instrs):
    bots, output = {}, {}
    types = {'bots':bots, 'output':output}

    for i in instrs:
        if len(i) == 2:
            bots[i[1]] = i[0]
        else:
            vals = sorted(bots[i[0]])
            for t in [1, 3]:
                types[i[t]] = vals[0]
                types[i][t+1] = vals[1]

def main():
    d = load_data()
    #parse(d)

if __name__ == '__main__':
    main()
