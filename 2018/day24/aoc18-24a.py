# AoC 2018 - Day 24a

from dataclasses import dataclass
from parse import parse
import logging

@dataclass
class Group:
    side: str
    name: str
    num: int
    hp: int
    dmg: int
    dmgtype: str
    init: int
    weak: list
    immune: list
    power = 0
    target = None
    is_targeted = False

def handle_weakimmune(instr):
    weak, immune = [], []
    instr = instr[1:-1].split(';') if ';' in instr else [instr[1:-1]]
    for part in instr:
        if 'weak to' in part:
            weak = [x.strip() for x in part[8:].split(', ')]
        if 'immune to' in part:
            immune = [x.strip() for x in part[10:].split(', ')]
    return weak, immune
        
def load_data():
    groups = []
    side = 'Immune'
    counter = 1

    with open('example.txt', 'r') as infile:
        for line in [x.strip() for x in infile.readlines()]:
            if not line or 'Immune System' in line:
                continue
            elif 'Infection' in line:
                side = 'Infection'
                counter = 1
            else:
                parsestr = '{} units each with {} hit points {} with an attack that does {} {} damage at initiative {}'
                num, hp, weakimm, dmg, dmgtype, init = parse(parsestr, line)
                weak, immune = handle_weakimmune(weakimm)
                name = f'{side} group {counter}'
                counter += 1
                groups.append(Group(side, name, int(num), int(hp), int(dmg), dmgtype, int(init), weak, immune))
    return groups

def show_status(groups):
    for side in ['Immune', 'Infection']:
        logging.debug(f'{side}:')
        for g in groups:
            if side in g.name:
                logging.debug(f'{g.name} contains {g.num} units.')

def sim_battle(groups):

    while True:
        for g in groups:
            g.power = g.num * g.dmg
            g.target = None
            g.is_targeted = False

        show_status(groups)

        for curr in sorted(groups, key=lambda x:(-x.power, -x.init)):
            poss = [g for g in groups if g.side != curr.side if g.is_targeted == False and curr.dmgtype not in g.immune]
            poss.sort(key=lambda x:(curr.dmgtype not in x.weak, -x.power, -x.init))
            if poss:
                curr.target = poss[0]
                poss[0].is_targeted = True
                logging.debug(f'{curr.name} targets {curr.target.name}')

        for curr in sorted([x for x in groups if x.target], key=lambda x:-x.init):
            dmgmult = 2 if curr.dmgtype in curr.target.weak else 1
            dmgdone = curr.power * dmgmult
            loss = dmgdone // curr.target.hp
            curr.target.num -= loss
            logging.debug(f'{curr.name} attacks {curr.target.name} for {dmgdone}, destroying {loss} units.')

        groups = [x for x in groups if x.num > 0]
        if len(set([x.side for x in groups])) == 1:
            return sum([x.num for x in groups])

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    groups = load_data()
    print(sim_battle(groups))

if __name__ == '__main__':
    main()
