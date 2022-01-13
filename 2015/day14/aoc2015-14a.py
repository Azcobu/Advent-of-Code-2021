# AoC 2015 - Day 14a
import parse

def load_data():
    reins = {}
    data = '''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'''
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    for x in data:
        name, fly, flydur, rest = parse.parse('{} can fly {} km/s for {} seconds, but then must rest for {} seconds.', x)
        reins[name] = (int(fly), int(flydur), int(rest))
    return reins

def calc_distances(reins, time):
    reinstats = {k: [v[1], 0, 0] for k, v in reins.items()} #flight, rest, total dist
    for currsec in range(time):
        for r, v in reinstats.items():
            if v[0] > 0: # flying
                v[2] += reins[r][0]
                v[0] -= 1
                if v[0] == 0: v[1] = reins[r][2]
            elif v[1] > 0: # resting
                v[1] -= 1
                if v[1] == 0:
                    v[0] = reins[r][1]
    return sorted(reinstats.items(), key=lambda x:x[1][2], reverse=True)

def main():
    data = load_data()
    print(calc_distances(data, 2503))

if __name__ == '__main__':
    main()
