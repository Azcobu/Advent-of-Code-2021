from parse import parse
import random

def load_data():
    probes = {}
    parsestr = 'pos=<{},{},{}>, r={}'
    with open('input.txt', 'r') as infile:
        for num, line in enumerate([x.strip() for x in infile.readlines()]):
            x, y, z, rad = [int(x) for x in parse(parsestr, line)]
            probes[num] = (x, y, z, rad)
    return probes

def gen_init_pop(probes, popsize):
    pop = {}
    min_x, max_x = min([x[0] for x in probes.values()]), max([x[0] for x in probes.values()])
    min_y, max_y = min([y[1] for y in probes.values()]), max([y[1] for y in probes.values()])
    min_z, max_z = min([z[2] for z in probes.values()]), max([z[2] for z in probes.values()])

    for x in range(popsize):
        pop[(random.randint(min_x, max_x), random.randint(min_y, max_y), random.randint(min_z, max_z))] = 0
    return pop

def calc_fitness(probes, pop):
    for pop_coords, pop_score in pop.items():
        for probe_num, probe_coords in probes.items():
            dist = sum([abs(pop_coords[x] - probe_coords[x]) for x in range(3)])
            if dist <= probe_coords[3]:
                pop_score += 1
    print(sorted(pop.items(), key=lambda x:x[1], reverse=True)[:10])

def find_in_rad(probes):
    count = 0
    bigprobe, bigcoords = sorted(probes.items(), key=lambda x:x[1][3])[-1]
    
    for k, v in probes.items():
        dist = sum([abs(bigcoords[x] - v[x]) for x in range(3)])
        if dist <= bigcoords[3]:
            count += 1
    return count

def main():
    data = load_data()
    print(find_in_rad(data))
    pop = gen_init_pop(data, 1000)
    calc_fitness(data, pop)

if __name__ == '__main__':
    main()
