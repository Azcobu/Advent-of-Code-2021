# AoC 2023 Day 6

def main():
    races = {41: 249, 77: 1362, 70: 1127, 96: 1011}
    #races = {7: 9, 15: 40, 30: 200}
    total = 1
    wins = 0

    for time, dist in races.items():
        wins = sum([1 for hold in range(1, time + 1) if (time - hold) * hold > dist])
        total *= wins
    print(total)

if __name__ == '__main__':
    main()
