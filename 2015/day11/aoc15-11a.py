# AoC 2015 - Day 11a
import re

def forbid_letters(instr):
    return not any([True for x in instr if x in ['i', 'o', 'l']])

def has_triple(instr):
    for x in instr[:-2]:
        if ord(x) <= ord('x') and x + chr(ord(x)+1) + chr(ord(x)+2) in instr:
            return True
    return False

def has_double(instr):
    return bool(re.match(r'^.*(.)\1.*(.)\2.*$', "".join(instr)))

def increment(instr):
    lastlett = chr(ord(instr[-1]) + 1) if ord(instr[-1]) < ord('z') else 'a'
    return instr[:-1] + lastlett if lastlett != 'a' else increment(instr[:-1]) + 'a'

def main():
    pwd = 'cqjxjnds'
    newpass = increment(pwd)
    while not (has_triple(newpass) and has_double(newpass) and forbid_letters(newpass)):
        newpass = increment(newpass)
    print(newpass)

if __name__ == '__main__':
    main()
