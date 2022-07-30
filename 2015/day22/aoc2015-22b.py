# AoC 2015 - Day 22b
import itertools, copy, random, logging

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
    def __init__(self, name, max_hp, armour=0, dmg=0, mana=0):
        self.name = name
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.armour = armour
        self.dmg = dmg
        self.mana = mana

    def __repr__(self):
        return f'Entity: {self.name}, HP: {self.curr_hp}, Arm: {self.armour}'

def decrement_effect_cds(player, boss, spells):
    for s in spells:
        if s.effect:
            if s.effect.curr_cd > 0:
                if s.effect.dmg:
                    boss.curr_hp -= s.effect.dmg
                    logging.debug(f'{s.name} deals {s.effect.dmg} damage; its timer is now {s.effect.curr_cd-1}.')
                if s.effect.mana:
                    player.mana += s.effect.mana
                    logging.debug(f'{s.name} provides {s.effect.mana} mana; its timer is now {s.effect.curr_cd-1}.')

                s.effect.curr_cd -= 1
                if s.effect.curr_cd == 0:
                    logging.debug(f'{s.name} wears off.')

def sim_fights(i_player, i_boss, i_spells):
    mana_results = {}
    #test_spells = [4, 2, 1, 2, 0]

    for fight in range(20000):
        mana_used = 0
        spells_used = []
        player, boss, spells = copy.deepcopy(i_player), copy.deepcopy(i_boss), copy.deepcopy(i_spells)

        while player.curr_hp > 0 and boss.curr_hp > 0:
            logging.debug(f'-- Player turn --\n- Player has {player.curr_hp} hp, {player.armour} armour, {player.mana} mana.')
            logging.debug(f'- Boss has {boss.curr_hp} hp.')

            player.curr_hp -= 1
            if player.curr_hp <= 0:
                break

            if mana_results:
                if mana_used > min(mana_results.values()):
                    break

            decrement_effect_cds(player, boss, spells)

            spell_choices = [s for s in spells if s.cost <= player.mana and (not s.effect or s.effect.curr_cd == 0)]
            if not spell_choices:
                break
            currspell = random.choice(spell_choices)
            logging.debug(f'Player casts {currspell.name}')

            spells_used.append(currspell.name)
            mana_used += currspell.cost
            player.mana -= currspell.cost

            if currspell.effect:
                currspell.effect.curr_cd = currspell.effect.base_cd
            boss.curr_hp -= currspell.dmg
            player.curr_hp = min(player.curr_hp + currspell.heal, player.max_hp)

            if spells[2].effect.curr_cd > 0: # shield
                player.armour = spells[2].effect.armour
            else:
                player.armour = 0

            #boss turn
            logging.debug(f'-- Boss turn --\n- Player has {player.curr_hp} hp, {player.armour} armour, {player.mana} mana.')
            logging.debug(f'- Boss has {boss.curr_hp} hp.')

            decrement_effect_cds(player, boss, spells)
            if boss.curr_hp > 0:
                boss_attack = max(boss.dmg - player.armour, 1)
                player.curr_hp -= max(boss.dmg - player.armour, 1)
                logging.debug(f'Boss attacks for {boss_attack} damage.')
            else:
                logging.debug('Boss dies.')

        if player.curr_hp > 0 and boss.curr_hp <= 0:
            mana_results[tuple(spells_used)] = mana_used
    
    return sorted(mana_results.items(), key=lambda x:x[1])[0]
 
def main():
    logging.basicConfig(level=logging.ERROR, format='%(message)s')
    test_boss = Entity('boss', 14, 0, 8)
    test_player = Entity('player', 10, 0, 0, 250)
    boss = Entity('boss', 58, 0, 9)
    player = Entity('player', 50, 0, 0, 500)
    spells = init_spells()
    print(sim_fights(player, boss, spells))

if __name__ == '__main__':
    main()
