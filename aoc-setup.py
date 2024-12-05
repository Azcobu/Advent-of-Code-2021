import os
import time
import requests

def load_session_cookie():
    with open('d:\\tmp\\advent-cookie.txt', 'r', encoding='utf-8') as infile:
        return infile.read()

cookie = load_session_cookie()
cookie_dict = {'session': cookie}

def main():
    basepath = 'e:\\code\\blw\\advent-of-code\\'
    years = [str(y) for y in range(2024, 2025)]

    for y in years:
        currpath = os.path.join(basepath, y)
        for d in range(1, 7):
            daynum = str(d).zfill(2)
            dirname = os.path.join(currpath, f'day{daynum}')

            if not os.path.exists(dirname):
                os.makedirs(dirname)
                print(f"Directory '{dirname}' created.")

            problem_url = f'https://adventofcode.com/{y}/day/{d}'
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
