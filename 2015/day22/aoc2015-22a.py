# AoC 2015 - Day 22a
import itertools, copy, random

class Spell:
    def __init__(self, name, cost, dmg=0, heal=0, effect=None):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.heal = heal
        self.effect = effect

    def __repr__(self):
        return f'Spell: {self.name}'

class Effect:
    def __init__(self, name, base_cd, dmg=0, armour=0, mana=0):
        self.name = name
        self.base_cd = base_cd
        self.curr_cd = 0
        self.dmg = dmg
        self.armour = armour
        self.mana = mana

    def __repr__(self):
        return f'Effect: {self.name}, {self.curr_cd} of {self.base_cd} turns left'

def init_spells():
    eff_shield = Effect('eff_shield', 6, 0, 7)
    eff_poison = Effect('eff_poison', 6, 3)
    eff_recharge = Effect('eff_recharge', 5, 0, 0, 101)

    spell_magmiss = Spell('magmiss', 53, 4)
    spell_drain = Spell('drain', 73, 2, 2)
    spell_shield = Spell('shield', 113, 0, 0, eff_shield)
    spell_poison = Spell('poison', 173, 0, 0, eff_poison)
    spell_recharge = Spell('recharge', 229, 0, 0, eff_recharge)
    return [spell_magmiss, spell_drain, spell_shield, spell_poison, spell_recharge]

class Entity:
    def __init__(self, name, curr_hp, max_hp, armour=0, dmg=0, mana=0):
        self.name = name
        self.curr_hp = curr_hp
        self.max_hp = max_hp
        self.armour = armour
        self.dmg = dmg
        self.mana = mana

    def __repr__(self):
        return f'Entity: {self.name}, HP: {self.curr_hp}, Arm: {self.armour}'

def decrement_effect_cds(player, boss, spells):
    for s in spells:
        if s.effect:
            if 0 < s.effect.curr_cd <= s.effect.base_cd:
                boss.curr_hp -= s.effect.dmg
                player.mana += s.effect.mana

            if s.effect.curr_cd > 0:
                s.effect.curr_cd -= 1

def sim_fights(i_player, i_boss, i_spells):
    mana_results = {}
    test_spells = [3, 0]

    for fight in range(100):
        mana_used = 0
        spells_used = []
        player, boss, spells = copy.deepcopy(i_player), copy.deepcopy(i_boss), copy.deepcopy(i_spells)

        while player.curr_hp > 0 and boss.curr_hp > 0:

            if mana_results:
                if mana_used > min(mana_results.values()):
                    break

            spell_choices = [s for s in spells if not s.effect or s.effect.curr_cd == 0]
            currspell = random.choice(spell_choices)
            spells_used.append(currspell.name)
            mana_used += currspell.cost
            if currspell.effect:
                currspell.effect.curr_cd = currspell.effect.base_cd
            boss.curr_hp -= currspell.dmg
            player.curr_hp = min(player.curr_hp + currspell.heal, player.max_hp)

            # handle effects
            decrement_effect_cds(player, boss, spells)

            if spells[2].effect.curr_cd > 0: # shield
                player.armour = spells[2].effect.armour
            else:
                player.armour = 0

            #boss turn
            decrement_effect_cds(player, boss, spells)
            player.curr_hp -= max(boss.dmg - player.armour, 1)

        if player.curr_hp > 0:
            mana_results[tuple(spells_used)] = mana_used
    
    #print(mana_results)
    return sorted(mana_results.items(), key=lambda x:x[1])[0]
 
def main():
    test_boss = Entity('boss', 13, 13, 0, 8)
    test_player = Entity('player', 10, 10, 0, 0, 250)
    spells = init_spells()
    print(sim_fights(test_player, test_boss, spells))

if __name__ == '__main__':
    main()
