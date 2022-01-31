import os
import requests
import time

# https://adventofcode.com/2019/day/17/input
cookie = # redacted, get from browser's inspector.
cookie_dict = {'session':cookie}

def main():
    basepath = 'D:\\Python\\Code\\Advent-of-Code-2021\\'
    years = [str(y) for y in range(2015, 2021)]

    for y in years:
        currpath = os.path.join(basepath, y)
        for d in range(1, 26):
            daynum = str(d).zfill(2)
            dirname = os.path.join(currpath, f'day{daynum}')
            # os.mkdir(dirname)
            fname = os.path.join(dirname, 'input.txt')
            url = f'https://adventofcode.com/{y}/day/{d}/input'
            try:
                r = requests.get(url, allow_redirects=True, cookies=cookie_dict)
                open(fname, 'wb').write(r.content)
            except Exception as err:
                print(err)
            else:
                print(f'Saved {y} Day {d} input.')
                time.sleep(1)

if __name__ == '__main__':
    main()
