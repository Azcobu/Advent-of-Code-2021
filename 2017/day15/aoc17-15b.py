# AoC 2017 - Day 15b

def gen_1(g1):
    while True:
        g1 = (g1 * 16807) % 2147483647
        if g1 % 4 == 0:
            yield bin(g1)[-16:]

def gen_2(g2):
    while True:
        g2 = (g2 * 48271) % 2147483647
        if g2 % 8 == 0:
            yield bin(g2)[-16:]

def gen_comp(gen1, gen2):
    score = 0
    g1 = gen_1(gen1)
    g2 = gen_2(gen2)
    for x in range(5000000):
        if next(g1) == next(g2):
            score += 1
    return score

def main():
    print(gen_comp(699, 124))

if __name__ == '__main__':
    main()
