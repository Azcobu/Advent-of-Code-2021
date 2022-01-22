# AoC 2015 - Day 22a

class Effect:
    def __init__(self, name, turnsleft, dmg=0, armour=0, mana=0):
        self.name = name
        self.turnsleft = turnsleft
        self.dmg = dmg
        self.armour = armour
        self.mana = mana

    def __repr__(self):
        return f'Effect: {self.name}, {self.turnsleft} turns left'

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
    def __init__(self, name, hp, armour=0, dmg=0, mana=0):
        self.name = name
        self.hp = hp
        self.armour = armour

    def __rept__(self):
        return f'Entity: {self.name}, HP: {self.hp}, Arm: {self.armour}'

def main():
    boss = Entity('boss', 58, 0, 9)
    player = Entity('player', 50, 0, 0, 500)
    spells = init_spells()
    print(spells)

if __name__ == '__main__':
    main()
