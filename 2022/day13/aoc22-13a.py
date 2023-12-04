# AoC 2022 Day 13a

def load_data():
    with open('example.txt', 'r') as infile:
        return [x.strip() for x in infile.read().split('\n') if x]

def find_valid(data):
    count = 1
    left, right = data.pop(0), data.pop(0)
    
    while left and right:
        

def main():
    print(find_valid(load_data()))

if __name__ == '__main__':
    main()
