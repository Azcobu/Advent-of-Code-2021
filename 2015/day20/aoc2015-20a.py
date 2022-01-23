# AoC 2015 - Dy 20a
import math

def factorize(num):
    base = {1, num}
    facts = {x for x in range(2, int(math.sqrt(num)) + 1) if not num % x}
    div = {num//x for x in facts}
    return base | facts | div

def find_target(target):
    for num in range(1, target):
        total = sum(f * 10 for f in factorize(num))
        if total >= target:
            return num

def main():
    print(find_target(29000000))

if __name__ == '__main__':
    main()
