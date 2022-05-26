# AoC 2017- Day 25a

rules = {('A', 0): (1, 1, 'B'),  ('A', 1): (0, -1, 'D'),
         ('B', 0): (1, 1, 'C'),  ('B', 1): (0, 1, 'F'),
         ('C', 0): (1, -1, 'C'), ('C', 1): (1, -1, 'A'),
         ('D', 0): (0, -1, 'E'), ('D', 1): (1, 1, 'A'),
         ('E', 0): (1, -1, 'A'), ('E', 1): (0, 1, 'B'),
         ('F', 0): (0, 1, 'C'),  ('F', 1): (0, 1, 'E')}

def turing(rules, steps, currstate='A'):
    tape = {}
    currpos = 0

    for s in range(steps):
        tape[currpos], move, currstate = rules[(currstate, tape.get(currpos, 0))]
        currpos += move

    return list(tape.values()).count(1)

def main():
    print(turing(rules, 12302209))

if __name__ == '__main__':
    main()
