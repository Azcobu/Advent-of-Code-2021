# AoC 2017 - Day 3b

def calc_val(target):
    sqrs = {(0, 0): 1}
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)] #u, l, d, r
    ns = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    currdir = 3 # r
    sidelen = 1
    maxsidelen = 1
    sidecount = 0
    currsqr = 0, 0
    sqrval = 1

    while sqrs[currsqr] < target:
        sqrval = 0
        newsqr = currsqr[0] + dirs[currdir][0], currsqr[1] + dirs[currdir][1]
        for n in ns:
            k = newsqr[0] + n[0], newsqr[1] + n[1]
            if k in sqrs:
                sqrs[newsqr] = sqrs.get(newsqr, 0) + sqrs[k]
        currsqr = newsqr
        sidelen += 1
        if sidelen >= maxsidelen:
            sidecount += 1
            sidelen = 0
            currdir = (currdir + 1) % 4
        if sidecount >= 2:
            sidecount = 0
            maxsidelen += 1

    return sqrs[currsqr]

def main():
    print(calc_val(265149))

if __name__ == '__main__':
    main()
