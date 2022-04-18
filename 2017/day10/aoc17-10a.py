# AoC 2017 - Day 10a

def load_data():
    with open('input.txt', 'r') as infile:
        return [int(x) for x in infile.read().split(',')]

def get_eles(startpos, n, inlist):
    out = []
    for num in range(n):
        takepos = (startpos + num) % len(inlist)
        out.append(inlist[takepos])
    return out

def rebuild(startpos, revlist, oldlist):
    for pos, x in enumerate(revlist):
        addpos = (startpos + pos) % len(oldlist)
        oldlist[addpos] = x
    return oldlist

def knothash(listsize, lens):
    nums = list(range(listsize))
    currpos, skip = 0, 0
    for l in lens:
        revlist = get_eles(currpos, l, nums)[::-1]
        nums = rebuild(currpos, revlist, nums)
        currpos = (currpos + l + skip) % len(nums)
        skip += 1
    return nums[0] * nums[1]

def main():
    d = load_data()
    print(knothash(5, [3, 4, 1, 5]))
    print(knothash(256, d))

if __name__ == '__main__':
    main()
