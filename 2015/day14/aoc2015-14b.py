# AoC 2015 - Day 14a
import parse

def load_data():
    reins = {}
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    for x in data:
        name, fly, flydur, rest = parse.parse('{} can fly {} km/s for {} seconds, but then must rest for {} seconds.', x)
        reins[name] = (int(fly), int(flydur), int(rest))
    return reins

def calc_distances(reins, time):
    leads = {k:0 for k in reins.keys()}
    reinstats = {k: [v[1], 0, 0] for k, v in reins.items()} #flight, rest, total dist
    for currsec in range(time):
        for r, v in reinstats.items():
            if v[0] > 0: # flying
                v[2] += reins[r][0]
                v[0] -= 1
                if v[0] == 0: v[1] = reins[r][2]
            elif v[1] > 0: # resting
                v[1] -= 1
                if v[1] == 0: v[0] = reins[r][1]

        currmax = max([x[2] for x in reinstats.values()])
        for k, v in reinstats.items():
            if v[2] == currmax:
                leads[k] = leads.get(k, 0) + 1

    return sorted(leads.items(), key=lambda x:x[1], reverse=True)

def main():
    data = load_data()
    print(calc_distances(data, 2503))

if __name__ == '__main__':
    main()
