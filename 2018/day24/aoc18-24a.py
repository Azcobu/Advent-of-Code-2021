# AoC 2018 - Day 24a

from dataclasses import dataclass
from parse import parse

@dataclass
class Group:
    side: str
    num: int
    hp: int
    dmg: int
    dmgtype: str
    init: int
    weak: list
    immune: list
    effectpow = 0
    targeting = None
    targeted = False

def load_data():
    groups = []
    side = 'immune'

    with open('input.txt', 'r') as infile:
        for line in [x.strip() for x in infile.readlines()]:
            if 'Infection' in line:
                side = 'infect'

            parsestr = '{} units each with {} hit points {} with an attack that does {} {} damage at initiative {}'
            num, hp, weak, dmg, dmgtype, init = parse(parsestr, line)
            units.append(Group(side, num, hp, dmg, dmgtype, init, weak, immune))
    return units

def sim_battle(groups):
    #set effect pow and reset targeting
    for g in groups:
        g.effectpow = g.num * g.dmg
        g.targeting = None
        g.targeted = False

    for curr in sorted(groups, key=lambda x:(x.effectpow, x.init), reverse=True):
        pass

def main():

    test = [Group('immune', 17, 5390, 4507, 'fire', 2, ['radiation', 'bludgeoning'], []), 
            Group('immune', 989, 1274, 25, 'slashing', 3, ['bludgeoning', 'slashing'], ['fire']),
            Group('infect', 801, 4706, 116, 'bludgeoning', 1, ['radiation'], []),
            Group('infect', 4485, 2961, 12, 'slashing', 4, ['fire', 'cold'], ['radiation'])]
    sim_battle(test)

if __name__ == '__main__':
    main()
