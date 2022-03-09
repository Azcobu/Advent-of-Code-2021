# AoC 2017 - Day 3a
import math

def calc_dist(num):
    sqr = 1
    while sqr ** 2 < num:
        sqr += 2
    sidelen = sqr - 1
    sideoffset = sidelen // 2
    sidemids = [sqr ** 2 - (x * sidelen) - sideoffset for x in range(4)]
    mindiff = min(abs(s - num) for s in sidemids)
    return sideoffset + mindiff

def main():
    print(calc_dist(265149))

if __name__ == '__main__':
    main()
