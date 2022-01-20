# AoC 2015 - Day 21b
import itertools
from math import ceil

class Entity:
    def __init__(self, name, dmg=0, armour=0, hp=0, cost=0):
        self.name = name
        self.dmg = dmg
        self.armour = armour
        self.hp = hp
        self.cost = cost

    def __repr__(self):
        return f'{self.name}'

weaps = [Entity('dagger', 4, 0, 0, 8), Entity('shortsword', 5, 0, 0, 10),
         Entity('warhammer', 6, 0, 0, 25), Entity('longsword', 7, 0, 0, 40),
         Entity('greataxe', 8, 0, 0, 74)]

armour = [Entity('leather', 0, 1, 0, 13), Entity('chain', 0, 2, 0, 31),
          Entity('splint', 0, 3, 0, 53), Entity('band', 0, 4, 0, 75),
          Entity('plate', 0, 5, 0, 102), Entity('none', 0, 0, 0, 0)]

ringbase = [Entity('dmg +1', 1, 0, 0, 25), Entity('dmg +2', 2, 0, 0, 50),
            Entity('dmg +3', 3, 0, 0, 100), Entity('def +1', 0, 1, 0, 20),
            Entity('def +2', 0, 2, 0, 40), Entity('def +3', 0, 3, 0, 80)]

rings = []
for x in range(3):
    rings += [x for x in itertools.combinations(ringbase, x)]

def gen_loadouts():
    loadouts = {}
    for l in itertools.product(weaps, armour):
        for r in rings:
            loadouts[l + r] = eval_loadout(l + r)
    return loadouts

def eval_loadout(loadout):
    cost = sum([x.cost for x in loadout])
    dmg = sum([x.dmg for x in loadout])
    armour = sum([x.armour for x in loadout])
    return cost, dmg, armour

def eval_combat(boss, player, loadouts):
    scores = {}
    for k, v in loadouts.items():
        player.dmg, player.armour = v[1], v[2]

        boss_rnds = ceil(boss.hp / max(player.dmg - boss.armour, 1))
        player_rnds = ceil(player.hp / max(boss.dmg - player.armour, 1))

        if player_rnds < boss_rnds:
            scores[k] = v[0]
    winner = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    return winner[0]

def main():
    boss = Entity('boss', 9, 2, 103)
    player = Entity('player', 0, 0, 100)
    loadouts = gen_loadouts()
    print(eval_combat(boss, player, loadouts))

if __name__ == '__main__':
    main()
