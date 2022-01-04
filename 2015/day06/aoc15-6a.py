# AoC 2015 - Day 6

def load_data():
    with open('input.txt', 'r') as infile:
        indata = [x.split() for x in infile]

    return [(x[-4], x[-3], x[-1]) for x in indata]

def count_lights(instrs):
    display = set()
    for instr in instrs:
        cmd, coords1, coords2 = instr
        xstart, ystart = coords1.split(',')
        xend, yend = coords2.split(',')
        for xpos in range(int(xstart), int(xend) + 1):
            for ypos in range(int(ystart), int(yend) + 1):
                if cmd == 'on' or (cmd == 'toggle' and (xpos, ypos) not in display):
                    display.add((xpos, ypos))
                elif cmd == 'off' or (cmd == 'toggle' and (xpos, ypos) in display):
                    display.discard((xpos, ypos))
    return len(display)

def main():
    data = load_data()
    #testdata = [('on', '0,0', '999,999'), ('toggle', '0,0', '999,0'), ('off', '499,499', '500,500')]
    #assert count_lights(testdata) == 998996
    print(count_lights(data))

if __name__ == '__main__':
    main()
