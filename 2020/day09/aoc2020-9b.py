
def load_data():
    nums = []
    with open('input.txt', 'r') as infile:
        return [int(x) for x in infile.read().splitlines()]

def find_contiguous(nums, target):
    total = 0
    for start, num in enumerate(nums):
        end = start + 1
        while sum(nums[start:end]) < target:
            end += 1
        if sum(nums[start:end]) == target:
            return min(nums[start:end]) + max(nums[start:end])

def main():
    print(find_contiguous(load_data(), 248131121)) 

if __name__ == '__main__':
    main()
