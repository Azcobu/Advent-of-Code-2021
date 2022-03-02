# AoC 2016 - Day 21b
from itertools import permutations

def parse_instrs(instr):
    instr = list(instr)
    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            nums = [int(x) for x in line.strip().split(' ') if x.isnumeric()]
            if 'move position' in line:
                instr = move_pos(instr, nums[0], nums[1])
            elif 'reverse positions' in line:
                instr = reverse_pos(instr, nums[0], nums[1])
            elif 'swap position' in line:
                instr = swap_pos(instr, nums[0], nums[1])
            elif 'swap letter' in line:
                instr = swap_letters(instr, line[12], line[-2])
            elif 'rotate based on position' in line:
                instr = rotate_letter(instr, line[-2])
            elif 'rotate' in line:
                rot = nums[0]
                if 'left' in line: rot *= -1
                instr = rotate_steps(instr, rot)
    return ''.join(instr)

def swap_pos(inlist, x, y):
    inlist[x], inlist[y] = inlist[y], inlist[x]
    return inlist

def move_pos(inlist, x, y):
    movechar = inlist.pop(x)
    inlist.insert(y, movechar)
    return inlist

def swap_letters(inlist, x, y):
    xpos, ypos = inlist.index(x), inlist.index(y)
    inlist[xpos], inlist[ypos] = inlist[ypos], inlist[xpos]
    return inlist

def rotate_steps(inlist, steps):
    steps %= len(inlist)
    steps *= -1
    return inlist[steps:] + inlist[:steps]

def rotate_letter(inlist, letter):
    index = inlist.index(letter)
    steps = index + 2 if index >= 4 else index + 1
    return rotate_steps(inlist, steps)

def reverse_pos(inlist, x, y):
    rev = inlist[x:y+1]
    rev.reverse()
    return inlist[:x] + rev + inlist[y+1:]

def main():
    for k in permutations('fbgdceah'):
        if parse_instrs(k) == 'fbgdceah':
            print(''.join(k))
            break

if __name__ == '__main__':
    main()
