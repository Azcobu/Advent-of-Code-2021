# AoC 2022 Day 4b

def load_data():
    assigns = []
    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            line = ''.join([x if x.isdigit() else ' ' for x in line])
            assigns.append([int(x) for x in line.split(' ') if x.isdigit()])
    return assigns

def count_overlaps(assigns):
    total = 0
    for a in assigns:
        a1 = {x for x in range(a[0], a[1] + 1)}
        a2 = {x for x in range(a[2], a[3] + 1)}
        if a1 & a2:
            total += 1
    return total

def main():
    print(count_overlaps(load_data()))

if __name__ == '__main__':
    main()
