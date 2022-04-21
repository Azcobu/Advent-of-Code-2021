# AoC 2017 - Day 17b

def spinlock(step):
    currpos, afterzero = 0, 0

    for x in range(1, 50000001):
        currpos = (currpos + step) % x + 1
        if currpos == 1:
            afterzero = x
    return afterzero

def main():
    print(spinlock(335))

if __name__ == '__main__':
    main()
