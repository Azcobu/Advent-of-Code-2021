# AoC Day 18b

class NewNum:
    def __init__(self, val):
        self.val = val

    def __add__(self, val2):
        return NewNum(self.val * val2.val)

    def __mul__(self, val2):
        return NewNum(self.val + val2.val)

def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    return [process_str(x) for x in d]

def process_str(instr):
    return [x for x in instr if x != ' ']

def translate(expr):
    tdict = {'*':'+', '+':'*', '(':'(', ')':')'}
    return ' '.join([tdict[x] if x in tdict else f'NewNum({x})' for x in expr])

def eval_all(inlist):
    return sum([eval(translate(x)).val for x in inlist])
    
def main():
    print(eval_all(load_data()))

if __name__ == '__main__':
    main()
