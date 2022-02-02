# AoC 15 Day 12a
import re
import json

# \{*:"red"*  \}

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read()

def hook(obj):
  return {} if "red" in obj.values() else obj

def main():
    data = load_data()
    scan = str(json.loads(data, object_hook=hook))
    print(sum(map(int, re.findall("-?[0-9]+", scan))))

if __name__ == '__main__':
    main()
