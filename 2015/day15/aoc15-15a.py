# AoC 2015 - Day 15a
import itertools
from math import prod
from parse import parse

def load_data():
    ingreds = {}
    with open('input.txt', 'r') as infile:
        indata = [x.strip() for x in infile]
    for line in indata:
        parsestr = '{}: capacity {}, durability {}, flavor {}, texture {}, calories {}'
        ingred, capa, dura, flav, text, calo = parse(parsestr, line)
        ingreds[ingred] = (int(capa), int(dura), int(flav), int(text), int(calo))
    return ingreds

def calc_score(ingreds, recipe):
    score = [0, 0, 0, 0]
    for qual in range(4):
        for ingred, amount in recipe.items():
            score[qual] += ingreds[ingred][qual] * amount
    return prod([0 if x < 0 else x for x in score])

def gen_recipes(ingreds, maxnum):
    for x in itertools.combinations_with_replacement(ingreds.keys(), maxnum):
        vals = {}
        counts = [x.count(y) for y in ingreds.keys()]
        for num, item in enumerate(ingreds):
            vals[item] = counts[num]
        yield vals

def find_best(ingreds, maxnum):
    scores = {str(r):calc_score(ingreds, r) for r in gen_recipes(ingreds, maxnum)}
    return sorted(scores.items(), key=lambda x:x[1], reverse=True)[0]

def main():
    ingreds = load_data()
    print(find_best(ingreds, 100))

if __name__ == '__main__':
    main()
