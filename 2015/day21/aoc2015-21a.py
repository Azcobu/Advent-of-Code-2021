# AoC 2015 - Day 21a
import itertools

class Entity:
    def __init__(self, name, dmg=0, armour=0, hp=0, cost=0):
        self.name = name
        self.dmg = dmg
        self.armour = armour
        self.hp = hp
        self.cost = cost

    def __repr__(self):
        outstr = f'Name: {self.name}: '
        if self.hp: outstr += 'hp {self.hp}, '
        if self.cost: outstr += f'cost {self.cost}, '
        return outstr + f'dmg {self.dmg}, armour {self.armour}'

weaps = [Entity('dagger', 4, 0, 0, 8), Entity('shortsword', 5, 0, 0, 10),
         Entity('warhammer', 6, 0, 0, 25), Entity('longsword', 7, 0, 0, 40),
         Entity('greataxe', 8, 0, 0, 74)]

armour = [Entity('leather', 0, 1, 0, 13), Entity('chain', 0, 2, 0, 31),
          Entity('splint', 0, 3, 0, 53), Entity('band', 0, 4, 0, 75),
          Entity('plate', 0, 5, 0, 102), Entity('none', 0, 0, 0, 0)]

rings = [Entity('dmg +1', 1, 0, 0, 25), Entity('dmg +2', 2, 0, 0, 50),
         Entity('dmg +3', 3, 0, 0, 100), Entity('def +1', 0, 1, 0, 20),
         Entity('def +2', 0, 2, 0, 40), Entity('def +3', 0, 3, 0, 80)]

def gen_loadout():
    totals = {}
    currload = []
    for w in weaps:
        for a in armour: #how handle no arm?
            for k in range(3):
                for ringset in itertools.combinations(rings, k):
                    currload.append(w) # = [w, a, r] if r else [w, a]
                    cost = sum([x.cost for x in loadout])
                    totals[cost]
    return totals

def calc_dmg(att_dmg, def_arm):
    return max(att_dmg - def_arm, 1)

#def resolve(entity1, entity2)

def main():
    print(gen_loadout())

if __name__ == '__main__':
    main()
