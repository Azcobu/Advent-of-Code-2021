# AoC 2017 - Day 15b

def gen_comp(gen1, gen2):
    score = 0
    for x in range(40000000):
        gen1 = gen1 * 16807 % 2147483647
        gen2 = gen2 * 48271 % 2147483647
        if bin(gen1)[-16:] == bin(gen2)[-16:]:
            score += 1
    return score

def main():
    print(gen_comp(699, 124))

if __name__ == '__main__':
    main()
