# AoC 2017 - Day 10b
from functools import reduce

def load_data(instr):
    return [ord(x) for x in instr] + [17, 31, 73, 47, 23]

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

def calc_knothash(listsize, lens):
    currpos, skip = 0, 0
    nums = list(range(listsize))

    for r in range(64):
        for l in lens:
            revlist = get_eles(currpos, l, nums)[::-1]
            nums = rebuild(currpos, revlist, nums)
            currpos = (currpos + l + skip) % len(nums)
            skip += 1
    return process_hash(nums)

def process_hash(inlist):
    out = []
    for x in range(16):
        bytestr = inlist[x*16:x*16+16]
        out.append(reduce(lambda x, y: x^y, bytestr))
    return ''.join([hex(x)[2:].zfill(2) for x in out])

def knothash(instr):
    return calc_knothash(256, load_data(instr))

def main():
    tests = {'':'a2582a3a0e66e6e86e3812dcb672a272',
             'AoC 2017': '33efeb34ea91902bb2f59c9920caa6cd',
             '1,2,3':'3efbe78a8d82f29979031a4aa0b16a9d',
             '1,2,4':'63960835bcdc130f0b66d7ff4f6a5a8e'}
    for k, v in tests.items():
        assert knothash(256, load_data(k)) == v
    print(knothash(256, load_data('file')))

if __name__ == '__main__':
    main()
