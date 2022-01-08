# AoC 2015 - Day 10

def look_say(instr):
    seqs = []
    while instr:
        currchar = instr[0]
        pos = 1
        while pos < len(instr):
            if instr[pos] == currchar:
                pos += 1
            else:
                break
        seqs.append(str(pos))
        seqs.append(currchar)
        instr = instr[pos:]
    return ''.join(seqs)

def main():
    res = '1113122113'
    for x in range(40):
        res = look_say(res)
    #print(res)
    print(len(res))

if __name__ == '__main__':
    main()
