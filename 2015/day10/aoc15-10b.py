# AoC 2015 - Day 10b

def look_say(instr):
    seqs = []
    currpos = 0
    while currpos < len(instr):
        currchar = instr[currpos]
        nextpos = 1
        while currpos + nextpos < len(instr):
            if instr[currpos + nextpos] == currchar:
                nextpos += 1
            else:
                break
        seqs.extend([str(nextpos), currchar])
        currpos += nextpos
    return ''.join(seqs)

def main():
    res = '1113122113'
    for x in range(50):
        print(x)
        res = look_say(res)
    print(len(res))

if __name__ == '__main__':
    main()
