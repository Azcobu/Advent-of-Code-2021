# AoC 2020 Day 5a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def bin_part(instr, start, end):
    pivot = (start + end) // 2 
    for c in instr:
        if c in ['F', 'L']:
            end = pivot
        else:
            start = pivot + 1
        pivot = (start + end) // 2 
    return start if c in ['F', 'L'] else end

def find_id(instr):
    return bin_part(instr[:7], 0, 127) * 8 + bin_part(instr[7:], 0, 7)

def find_missing(data):
    all_ids = [find_id(x) for x in data]
    return set(range(min(all_ids), max(all_ids))) - set(all_ids)

def main():
    print(find_missing(load_data()))

if __name__ == '__main__':
    main()