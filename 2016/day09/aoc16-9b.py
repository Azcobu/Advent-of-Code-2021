# AoC 2016 9b
import parse

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().strip()

def calc_len(instr):
    start, end = instr.find('('), instr.find(')') + 1
    if start != -1:
        strlen, repeats = parse.parse('({:d}x{:d})', instr[start:end])
        repstr = instr[end:end+strlen]
        return len(instr[:start]) + calc_len(repstr) * repeats + calc_len(instr[end+strlen:])
    else:
        return len(instr)

def main():
    assert calc_len('X(8x2)(3x3)ABCY') == 20
    assert calc_len('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
    assert calc_len('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445
    print(calc_len(load_data()))

if __name__ == '__main__':
    main()
