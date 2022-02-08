from collections import Counter
from operator import itemgetter

instr = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]',
'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def validate_rooms(instr):
    sector_ids = []
    for room in instr:
        c = Counter([x for x in room.rpartition('-')[0] if x != '-'])
        alpha = sorted(c.items(), key=itemgetter(0))
        freq = sorted(alpha, key=itemgetter(1), reverse=True)
        check = ''.join([x[0] for x in freq][:5])
        bpos = room.find('[')
        if check == room[bpos+1:bpos+6]:
            sector_ids.append(int(''.join([x for x in room if x.isnumeric()])))
    return sum(sector_ids)

def main():
    assert validate_rooms(instr) == 1514
    print(validate_rooms(load_data()))

if __name__ == '__main__':
    main()
