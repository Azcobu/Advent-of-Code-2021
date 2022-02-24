from  hashlib import md5
from collections import deque

def hash_str(instr, loop=0):
    for x in range(loop + 1):
        out = md5(instr.encode('utf-8')).hexdigest()
        instr = out
    return out

def find_keys(salt, repeats):
    index = 0
    foundkeys = []

    hashes = deque([hash_str(f'{salt}{x}', repeats) for x in range(1001)], 1001)
    while len(foundkeys) < 64:
        for pos, char in enumerate(hashes[0][:-2]):
            if char == hashes[0][pos+1] == hashes[0][pos+2]:
                for i in range(1, 1001):
                    if char*5 in hashes[i]:
                        foundkeys.append(index)
                        print(f'Found key {len(foundkeys)} at {index}.')
                        break
                break
        index += 1
        hashes.append(hash_str(f'{salt}{index + 1000}', repeats))
    return foundkeys[63]

def main():
    print(find_keys('yjdafjpo', 2016))

if __name__ == '__main__':
    main()
