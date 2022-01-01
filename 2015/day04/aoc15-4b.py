import hashlib
import itertools

def find_target(prefix):
    for x in itertools.count():
        cand = prefix + str(x)
        md5str = hashlib.md5(cand.encode('utf-8')).hexdigest()
        if md5str.startswith('000000'):
            return x

def main():
    print(find_target('ckczppom'))

if __name__ == '__main__':
    main()
