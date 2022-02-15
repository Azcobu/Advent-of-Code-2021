# AoC 2016 9a
import parse

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().strip()

def decompress_len(instr):
    outstr = []
    while '(' in instr:
        start, end = instr.find('('), instr.find(')')
        outstr.append(instr[:start])
        strlen, repeats = parse.parse('({:d}x{:d})', instr[start:end+1])
        repstr = instr[end+1:end+1+strlen]
        outstr.append(repstr * repeats)
        instr = instr[end+1+strlen:]
    outstr.append(instr)
    return len(''.join(outstr))

def main():
    assert decompress_len('ADVENT') == 6
    assert decompress_len('A(1x5)BC') == 7
    assert decompress_len('(3x3)XYZ') == 9
    assert decompress_len('A(2x2)BCD(2x2)EFG') == 11
    assert decompress_len('(6x1)(1x3)A') == 6
    assert decompress_len('X(8x2)(3x3)ABCY') == 18
    print(decompress_len(load_data()))

if __name__ == '__main__':
    main()
