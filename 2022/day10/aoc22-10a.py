# AoC 2022 Day 10a

def load_data():
    with open('input.txt', 'r') as infile:
        return [(x[:4], int(x[5:])) if 'addx' in x else ('noop',) for x in infile.readlines()]

def track_sigstr(instrs):
    x, cycle, sigstr = 1, 0, 0
    k = [20, 60, 100, 140, 180, 220]

    for instr in instrs:
        if instr[0] == 'addx':
            for tick in range(2):
                cycle += 1
                if cycle in k: sigstr += k.pop(0) * x
            x += instr[1]
        else:
            cycle += 1
            if cycle in k: sigstr += k.pop(0) * x

    return sigstr

def main():
    print(track_sigstr(load_data()))

if __name__ == '__main__':
    main()
