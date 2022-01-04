# AoC 2015 - Day 6b

def load_data():
    with open('input.txt', 'r') as infile:
        indata = [x.split() for x in infile]
    return [(x[-4], x[-3], x[-1]) for x in indata]

def count_lights(instrs):
    display = {}
    for instr in instrs:
        cmd, coords1, coords2 = instr
        xstart, ystart = coords1.split(',')
        xend, yend = coords2.split(',')
        for xpos in range(int(xstart), int(xend) + 1):
            for ypos in range(int(ystart), int(yend) + 1):
                if cmd == 'on':
                    display[(xpos, ypos)] = display.get((xpos, ypos), 0) + 1
                elif cmd == 'off':
                    display[(xpos, ypos)] = display.get((xpos, ypos), 0) - 1
                    if display[(xpos, ypos)] <= 0:
                        del display[(xpos, ypos)]
                elif cmd == 'toggle':
                    display[(xpos, ypos)] = display.get((xpos, ypos), 0) + 2

    return sum([x for x in display.values()])

def main():
    data = load_data()
    print(count_lights(data))

if __name__ == '__main__':
    main()
