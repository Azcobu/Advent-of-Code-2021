# AoC 2015 - Day 22a

class Effect:
    def __init__(self, name, base_cooldown, dmg=0, armour=0, mana=0):
        self.name = name
        self.base_cooldown = base_cooldown
        self.curr_cooldown = 0
        self.dmg = dmg
        self.armour = armour
        self.mana = mana

    def __repr__(self):
        return f'Effect: {self.name}, {self.cooldown} turns left'

class Spell:
    def __init__(self, name, cost, dmg=0, heal=0, effect=None):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.heal = heal
        self.effect = effect

    def __repr__(self):
        return f'Spell: {self.name}'

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

def poss_casts(spells):
    return [s for s in spells if not s.effect or s.effect.curr_cooldown == 0]

def sim_combat(player, boss, spells, castorder):
    mana_used = []
    for c in castorder:
        currspell = spells[c]
        mana_used.append(currspell.cost)
        if currspell.effect:
            currspell.curr_cooldown = currspell.base_cooldown
        boss.curr_hp -= currspell.dmg
        player.curr_hp = min(player.curr_hp + currspell.heal, player.max_hp)

        # handle effects
        for s in spells[]:
            if s.effect:
                if 0 < s.effect.curr_cooldown < s.effect.max_cooldown:
                    boss.hp -= s.effect.dmg
                    player.mana += s.effect.mana

                if s.effect.curr_cooldown > 0:
                    s.effect.cooldown -= 1

            if s.name == 'Shield' and s.effect.curr_cooldown > 0:
                player.armour = s.effect.armour
            else:
                player.armour = 0

        #boss turn
        player.curr_hp -= max(boss.dmg - player.armour, 1)
        if player.curr_hp <= 0:
            return None

def main():
    boss = Entity('boss', 58, 58, 0, 9)
    player = Entity('player', 50, 50, 0, 0, 500)
    spells = init_spells()
    castorder = [0, 1, 0]
    print(sim_combat(player, boss, spells, castorder))

if __name__ == '__main__':
    main()
