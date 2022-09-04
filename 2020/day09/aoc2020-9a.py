
def load_data():
    nums = []
    with open('input.txt', 'r') as infile:
        return [int(x) for x in infile.read().splitlines()]

def find_invalid(nums, window):
    winset = set()

    for pos, num in enumerate(nums[window:]):
        winset = set(nums[pos:pos+window])
        for x in winset:
            if num - x in winset:
                break
        else:
            return num

def main():
    print(find_invalid(load_data(), 25))

if __name__ == '__main__':
    main()
