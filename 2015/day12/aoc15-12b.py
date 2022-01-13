# AoC 15 Day 12a
import re

# \{*:"red"*  \}

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.readlines()

def main():
    data = load_data()
    for x in data:
        if re.findall('\{.*:"red".*\}', x):
            print(x)

if __name__ == '__main__':
    main()
