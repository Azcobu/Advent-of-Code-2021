# AoC 2022 - Day 6a

def load_data():
    moves = []
    with open('input.txt', 'r') as infile:
        return infile.read().strip()

def find_marker(instr):
    for pos in range(len(instr) - 3):
        currstr = instr[pos:pos+4]
        if len(set(currstr)) == 4:
            return pos + 4

def main():
    assert find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
    assert find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert find_marker('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
    print(find_marker(load_data()))

if __name__ == '__main__':
    main()
