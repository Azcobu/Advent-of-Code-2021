# AoC 2022 Day 2a

def load_data():
    strat = []
    with open('input.txt', 'r') as infile:
        d = infile.readlines()
    for line in d:
        strat.append(line.strip().split(' '))
    return strat

def calc_score(strat):
    # A for Rock, B for Paper, and C for Scissors
    # X for Rock, Y for Paper, and Z for Scissors
    # score += 1 for Rock, 2 for Paper, and 3 for Scissors
    # score += 0 if you lost, 3 if the round was a draw, and 6 if you won
    score = 0
    scores = {'A': {'X': 4, 'Y': 8, 'Z': 3}, 
              'B': {'X': 1, 'Y': 5, 'Z': 9},
              'C': {'X': 7, 'Y': 2, 'Z': 6}}
    return sum([scores[x][y] for x, y in strat])

def main():
    print(calc_score(load_data()))

if __name__ == '__main__':
    main()
