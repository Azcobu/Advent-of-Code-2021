# AoC 2015 - Dy 20a
import math

def factorize(num):
    found = {1, num}
    facts = {x for x in range(2, int(math.sqrt(num)) + 1) if not num % x}
    div = {num//x for x in facts}
    return found | facts | div

def find_target(target):
    for num in range(1, target):
        total = sum([f * 11 for f in factorize(num) if num <= 50 * f])
        if total >= target:
            return num

def main():
    print(find_target(29000000))

if __name__ == '__main__':
    main()
