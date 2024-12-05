# AoC 2024 Day 1a

def load_data() -> tuple:
    l1, l2 = [], []

    with open('input.txt', 'r', encoding='utf-8') as infile:
        for x in infile.readlines():
            a, b = x.strip().split()
            l1.append(int(a))
            l2.append(int(b))
    return sorted(l1), sorted(l2)

def main():
    l1, l2 = load_data()
    total = sum([abs(a - b) for a, b in zip(l1, l2)])
    print(total)

if __name__ == '__main__':
    main()
