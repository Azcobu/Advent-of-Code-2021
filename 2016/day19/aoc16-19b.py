# AoC 2016 - Day 19b
from collections import deque

def calc_winner(total):
    firsthalf, sechalf = deque(range(1, total//2+1)), deque(range(total//2 + 1, total + 1))

    while len(firsthalf) and len(sechalf):
        sechalf.popleft()
        if len(firsthalf) == len(sechalf):
            firsthalf.append(sechalf.popleft())
        sechalf.append(firsthalf.popleft())
    return sechalf[0]

def main():
    print(calc_winner(3004953))

if __name__ == '__main__':
    main()
