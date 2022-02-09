import hashlib

def find_pwd(door_id):
    pwd = ['_' for x in range(8)]
    num = 0

    while '_' in pwd:
        curr_hash = hashlib.md5(f'{door_id}{num}'.encode('utf-8')).hexdigest()
        if curr_hash.startswith('00000') and curr_hash[5].isdigit():
            pos = int(curr_hash[5])
            if pos in range(8) and pwd[pos] == '_':
                pwd[pos] = curr_hash[6]
                print(f'{"".join(pwd)} - {num}')
        num += 1
    return ''.join(pwd)

def main():
    print(find_pwd('uqwqemis'))

if __name__ == '__main__':
    main()
