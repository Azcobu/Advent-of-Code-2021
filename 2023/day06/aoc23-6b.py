# AoC 2023 Day 6

def main():
    races = {41777096: 249136211271011}
    #races = {71530: 940200}
    total = 1
    wins = 0

    for time, dist in races.items():
        wins = sum([1 for hold in range(1, time + 1) if (time - hold) * hold > dist])
        total *= wins
    print(total)

if __name__ == '__main__':
    main()
