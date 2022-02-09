import hashlib

def find_pwd(door_id):
    pwd = ''
    num = 0

    while len(pwd) < 8:
        curr_hash = hashlib.md5(f'{door_id}{num}'.encode('utf-8')).hexdigest()
        if curr_hash.startswith('00000'):
            pwd += curr_hash[5]
        num += 1
    return ''.join(pwd)

def main():
    print(find_pwd('uqwqemis'))

if __name__ == '__main__':
    main()
