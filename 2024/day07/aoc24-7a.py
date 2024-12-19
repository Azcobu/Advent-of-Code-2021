# AoC 24 - Day 7a

def load_data() -> list:
    equats = []
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for line in infile.readlines():
            target, _, nums = line.strip().partition(': ')
            equats.append([int(target)] + [int(x) for x in nums.split(' ')])
    return equats

def is_valid(target: int, nums: list, currtotal: int = 1):
    if not nums:
        return currtotal == target
    else:
        nextnum = nums[0]
        return (is_valid(target, nums[1:], currtotal + nextnum) or
                is_valid(target, nums[1:], currtotal * nextnum))

def main():
    equats = load_data()
    print(sum([e[0] for e in equats if is_valid(e[0], e[1:])]))

if __name__ == '__main__':
    main()
