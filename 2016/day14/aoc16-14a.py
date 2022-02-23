import hashlib
from collections import deque

def find_keys(salt):
    index = 0
    foundkeys = []

    hashes = deque([hashlib.md5(f'{salt}{x}'.encode('utf-8')).hexdigest() for x in range(1001)], 1001)
    while len(foundkeys) < 64:
        for c in hashes[0][:-2]:
            if c*3 in hashes[0]:
                for i in range(1001):
                    if c*5 in hashes[i]:
                        foundkeys.append(index)
                        break

        index += 1
        hashes.append(hashlib.md5(f'{salt}{index + 1000}'.encode('utf-8')).hexdigest())
    return foundkeys

def main():
    print(find_keys('abc'))

if __name__ == '__main__':
    main()
