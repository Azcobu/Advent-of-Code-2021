# AoC 2016 - Day 17b
from hashlib import md5

def valid_doors(x, y, password, path):
    valid = {}
    diffs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    dirs = ['U', 'D', 'L', 'R']
    currhash = md5(f'{password}{path}'.encode('utf-8')).hexdigest()
    for k in range(4):
        if currhash[k] in ['b', 'c', 'd', 'e', 'f']:
            new_x, new_y = x + diffs[k][0], y + diffs[k][1]
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                valid[dirs[k]] = (new_x, new_y)
    return valid

def navigate(x, y, password, path):
    if x == 3 and y == 3:
        yield len(path)
    else:
        for k, v in valid_doors(x, y, password, path).items():
            yield from navigate(v[0], v[1], password, path + k)

def nav_mngr(password):
    found = list(navigate(0, 0, password, ''))
    return sorted(found, reverse=True)[0]

def main():
    assert nav_mngr('ihgpwlah') == 370
    assert nav_mngr('kglvqrro') == 492
    assert nav_mngr('ulqzkmiv') == 830
    print(nav_mngr('edjrjqaa'))

if __name__ == '__main__':
    main()
