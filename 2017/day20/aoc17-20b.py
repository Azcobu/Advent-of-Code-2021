# AoC 2017 - 20a

from parse import parse
from dataclasses import dataclass
from math import sqrt

@dataclass
class Particle:
    num: int
    dist: int
    xpos: int
    ypos: int
    zpos: int
    xvel: int
    yvel: int
    zvel: int
    xacc: int
    yacc: int
    zacc: int

def load_data():
    parts = []
    with open('input.txt', 'r') as infile:
        for pnum, line in enumerate(infile):
            xpos, ypos, zpos, xvel, yvel, zvel, xacc, yacc, zacc =\
            parse('p=<{},{},{}>, v=<{},{},{}>, a=<{},{},{}>', line.strip())
            p = Particle(pnum, 0, int(xpos), int(ypos), int(zpos),
                                  int(xvel), int(yvel), int(zvel),
                                  int(xacc), int(yacc), int(zacc))
            parts.append(p)
    return parts

def calc_nearest(parts):
    for x in range(100):
        posdict = {}
        for p in parts:
            p.xvel += p.xacc
            p.yvel += p.yacc
            p.zvel += p.zacc
            p.xpos += p.xvel
            p.ypos += p.yvel
            p.zpos += p.zvel

            pos = (p.xpos, p.ypos, p.zpos)
            posdict[pos] = posdict.get(pos, []) + [p.num]

        for k, v in posdict.items():
            if len(v) > 1:
                parts = [x for x in parts if x.num not in v]

    return len(parts)

def main():
    p = load_data()
    print(calc_nearest(p))

if __name__ == '__main__':
    main()
