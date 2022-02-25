import os
import requests
import time
from bs4 import BeautifulSoup

def load_session_cookie():
    with open('d:\\tmp\\advent-cookie.txt', 'r') as infile:
        return infile.read()

cookie = load_session_cookie()
cookie_dict = {'session':cookie}

def main():
    basepath = 'e:\\code\\blw\\advent-of-code\\'
    years = [str(y) for y in range(2016, 2021)]

    for y in years:
        currpath = os.path.join(basepath, y)
        for d in range(1, 26):
            daynum = str(d).zfill(2)
            dirname = os.path.join(currpath, f'day{daynum}')
            problem_url = f'https://adventofcode.com/{y}/day/{d}'
            problem_fname = os.path.join(dirname, f'{y} Day {d} problem.html')
            input_url = problem_url + '/input'
            input_fname = os.path.join(dirname, 'input.txt')

            try:
                r = requests.get(input_url, allow_redirects=True, cookies=cookie_dict)
                open(input_fname, 'wb').write(r.content)
            except Exception as err:
                print(err)
            else:
                print(f'Saved {y} Day {d} problem and input.')
                time.sleep(1)

if __name__ == '__main__':
    main()
