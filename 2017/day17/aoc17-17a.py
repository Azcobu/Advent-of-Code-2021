# AoC 2017 - Day 17a

def spinlock(step):
    buffer = [0]
    currpos = 0

    for x in range(1, 2018):
        currpos = (currpos + step) % len(buffer) + 1
        buffer.insert(currpos, x)
    return buffer[currpos+1]

def main():
    assert spinlock(3) == 638
    print(spinlock(335))

if __name__ == '__main__':
    main()
