# Adent of Code 2021 - day 14a

from collections import Counter

indata = '''CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

def load_data(fname):
    rules = {}
    with open(fname, 'r') as infile:
        indata = infile.read()
    for x in indata.splitlines():
        k, v = x.split(' -> ')
        rules[k] = v.strip()
    return rules

def gen_startpairs(instr):
    pairs = {}
    for pos, x in enumerate(range(len(instr)-1)):
        newpair = instr[pos:pos+2]
        pairs[newpair] = pairs.get(newpair, 0) + 1
    return pairs

def iter_str(rules, paircount, steps):
    charcount = Counter() # ned to adjust counter for base input
    for step in range(steps):
        nextpairs = Counter(paircount)
        for pair, count in paircount.items():
            if pair in rules:
                nextpairs[pair] -= count
                nextpairs[pair[0] + rules[pair]] += count
                nextpairs[rules[pair] + pair[1]] += count
                charcount[rules[pair]] += count
        paircount = nextpairs

    print(paircount)
    return charcount

def main():
    fname = 'aoc21-14-input.txt'
    startstr = 'OKSBBKHFBPVNOBKHBPCO'
    rules = load_data(fname)
    startpairs = gen_startpairs(startstr)
    startchars = Counter(startstr)
    # After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times
    paircount = Counter(startpairs)
    iter_charcount = iter_str(rules, paircount, 40)
    totals = iter_charcount + startchars
    print(max(totals.values()) - min(totals.values()))

if __name__ == '__main__':
    main()
