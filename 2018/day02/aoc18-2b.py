# AoC 2018 - Day 2b

def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.readlines()
        return [x.strip() for x in d]

def find_match(data):
    for x in data:
        for y in data:
            count = 0
            common = []
            for diff in zip(x, y):
                if diff[0] != diff[1]:
                    count += 1
                else:
                    common.append(diff[0])
            if count == 1:
                print(f'{x} - {y} - commom is {"".join(common)}')
            
def main():
    data = load_data()
    find_match(data)

if __name__ == '__main__':
    main()
