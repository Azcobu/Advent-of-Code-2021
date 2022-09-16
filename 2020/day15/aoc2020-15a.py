# AoC 2020 Day 15a
from collections import defaultdict

def gen_sequence(seq):
    nums = defaultdict(list, {k: [pos + 1] for pos, k in enumerate(seq)})
    t = len(seq) + 1
    lastnum = seq[-1]

    for turn in range(t, 2021):
        if len(nums[lastnum]) <= 1:
            lastnum = 0
        else:
            lastnum = nums[lastnum][-1] - nums[lastnum][-2]
        nums[lastnum].append(turn)
    return lastnum

def main():
    assert gen_sequence([0, 3, 6]) == 436
    assert gen_sequence([1, 3, 2]) == 1
    assert gen_sequence([2, 1, 3]) == 10
    assert gen_sequence([1, 2, 3]) == 27
    assert gen_sequence([2, 3, 1]) == 78
    assert gen_sequence([3, 2, 1]) == 438
    assert gen_sequence([3, 1, 2]) == 1836
    print(gen_sequence([0,14,6,20,1,4]))


if __name__ == '__main__':
    main()
