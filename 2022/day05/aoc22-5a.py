#AoC 2022 Day 5a
from collections import deque
import re

def load_data():
    moves = []
    with open('input.txt', 'r') as infile:
        data = [x for x in infile.readlines()]
    pos = 0
    while '[' in data[pos]:
        pos += 1
    numstacks = max([int(x) for x in data[pos] if x.isdigit()])

    stacks = {x + 1: deque() for x in range(numstacks)}
    for linenum in range(pos):
        for letpos, letter in enumerate(data[linenum]):
            if letter.isalpha():
                stacks[letpos//4+1].append(letter)

    for linenum in range(pos+2, len(data)):
        x, y, z = [int(x) for x in re.findall(r'\d+', data[linenum])]
        moves.append((x, y, z))
    return stacks, moves

def find_tops(stacks, moves):
    for move in moves:
        num, move_from, move_to = move
        for _ in range(num):
            curr = stacks[move_from].popleft()
            stacks[move_to].appendleft(curr)
    return ''.join([stacks[x+1][0] for x in range(len(stacks))])

def main():
    s, m = load_data()
    print(find_tops(s, m))

if __name__ == '__main__':
    main()
