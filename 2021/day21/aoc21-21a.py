#AoC 21 - Day 21 - Dirac Dice

def dirac_dice(p1_start, p2_start):
    state = {1: 0, 2: 0, 'pos': [p1_start, p2_start]}
    numrolls = 0
    dieval = 1

    while True:
        for p in [1, 2]:
            newpos = (3 * dieval + 3 + state['pos'][p-1]) % 10 or 10
            state[p] += newpos
            state['pos'][p-1] = newpos
            dieval += 3
            numrolls += 3
            if state[p] >= 1000:
                print(state, numrolls)
                return min(state[1], state[2]) * numrolls

def main():
    r = dirac_dice(10, 1)
    print(r)

if __name__ == '__main__':
    main()
