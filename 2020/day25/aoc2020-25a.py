# AoC 2020 Day 25a

def find_loopsize(subj, target):
    val, loopsize = 1, 0
    while val != target:
        val = (val * subj) % 20201227
        loopsize += 1
    return loopsize

def main():
    card, door = 11349501, 5107328
    cardloop = find_loopsize(7, card)
    print(pow(door, cardloop, 20201227))

if __name__ == '__main__':
    main()
