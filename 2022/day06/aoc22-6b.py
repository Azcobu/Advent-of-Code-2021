# AoC 2022 - Day 6a

def load_data():
    moves = []
    with open('input.txt', 'r') as infile:
        return infile.read().strip()

def find_marker(instr):
    for pos in range(len(instr) - 13):
        currstr = instr[pos:pos+14]
        if len(set(currstr)) == 14:
            return pos + 14

def main():
    assert find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
    assert find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
    assert find_marker('nppdvjthqldpwncqszvftbrmjlhg') == 23
    assert find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
    assert find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26
    print(find_marker(load_data()))

if __name__ == '__main__':
    main()
