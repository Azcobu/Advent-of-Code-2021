# AoC 2016 - Day 11a
# elevator carries max 2 items and min of 1, stopping at every floor.
from itertools import combinations
from copy import copy


state = {'thul-chip':1, 'thul-gen':1, 'plut-chip':2, 'plut-gen':1, 'stron-chip':2,
         'stron-gen':1, 'prom-chip':3, 'prom-gen':3, 'ruth-chip':3, 'ruth-gen':3}
eles = ['thul', 'plut', 'stron', 'prom', 'ruth']

state = {'hydro-chip':1, 'lith-chip':1, 'hydro-gen':2, 'lith-gen':3}
eles = ['hydro', 'lith']

def is_valid(state):
    genlocs = [v for k, v in state.items() if '-gen' in k]
    for e in eles:
        if state[e+'-chip'] != state[e+'-gen'] and state[e+'-chip'] in genlocs:
            return False
    return True

def is_finished(state):
    for k, v in state.items():
        if v != 4:
            return False
    return True

def this_floor(state, floor):
    return [k for k, v in state.items() if v == floor]

def generate_combos(items):
    combs = [[x] for x in items] # single items
    for k in combinations(items, 2):
        combs += [list(k)]
    return combs

def valid_floors(curr_floor):
    valid = [curr_floor + 1, curr_floor - 1]
    return [x for x in valid if x > 0 and x <= 4]

def validate_move(state, move):
    newstate = copy(state)
    for item in move[2]:
        newstate[item] = move[1]
    return newstate if is_valid(newstate) else None

def find_path(state, path, currfloor, oldstates):
    if is_finished(state):
        if len(path) < find_path.minlen:
            find_path.minlen = len(path)
            yield path
    else:
        if len(path) < find_path.minlen:
            items = this_floor(state, currfloor)
            combos = generate_combos(items)
            for f in valid_floors(currfloor):
                for c in combos:
                    newmove = [currfloor, f, c]
                    newstate = validate_move(state, newmove)
                    if newstate and newstate not in oldstates:
                        yield from find_path(newstate, path + [newmove], f, oldstates + [newstate])

def path_mngr(state):
    find_path.minlen = 40
    for x in find_path(state, [], 1, [state]):
        print(f'{x} - len {len(x)}')
        print('---------------------------')

def main():
    path_mngr(state)

if __name__ == '__main__':
    main()
