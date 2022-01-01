import hashlib

def find_target(prefix):
    for x in range(10000000):
        cand = prefix + str(x)
        md5str = hashlib.md5(cand.encode('utf-8')).hexdigest()
        if md5str.startswith('00000'):
            return x

def main():
    assert find_target('abcdef') == 609043
    assert find_target('pqrstuv') == 1048970
    print(find_target('ckczppom'))

if __name__ == '__main__':
    main()
