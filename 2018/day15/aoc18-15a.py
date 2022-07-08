from dataclasses import dataclass

@dataclass
class Unit:
    type: str
    pos: tuple
    hp: int = 200
    attack: int = 3

def load_data():
    grid, elves, goblins = {}, [], []
    #with open('test-input.txt', 'r') as infile:
    with open('input.txt', 'r') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, char in enumerate(row):
                if char not in ['.', '\n']:
                    if char == 'E':
                        elves.append(Unit(char, (colnum, rownum)))
                    elif char == 'G':
                        goblins.append(Unit(char, (colnum, rownum)))
                    else:
                        grid[(colnum, rownum)] = char
    return grid, elves, goblins

def sim_battle(grid, elves, goblins):

    while elves and goblins:
        for unit in sorted(elves + goblins, key=lambda x:x.pos):
            currtype = unit.type
            #if in range, attack
            #else move

def main():
    print(load_data())

if __name__ == '__main__':
    main()
