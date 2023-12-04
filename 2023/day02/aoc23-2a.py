# AoC 2023 Day 2a

def load_data() -> dict:
    games = {}
    gamenum = 1
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for line in infile.readlines():
            games[gamenum] = {'red': 0, 'green': 0, 'blue': 0}
            line = line.partition(':')[2].replace(';', ',')
            for seg in line.split(','):
                seg = seg.strip()
                for col in ['red', 'green', 'blue']:
                    if col in seg:
                        num = int(seg.split(' ')[0])
                        if num > games[gamenum][col]:
                            games[gamenum][col] = num
            gamenum += 1
    return games

def main():
    possgames = 0

    games = load_data()
    for k, v in games.items():
        if v['red'] <= 12 and v['green'] <= 13 and v['blue'] <= 14:
            possgames += k

    print(possgames)

if __name__ == '__main__':
    main()
