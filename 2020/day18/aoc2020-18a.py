# AoC Day 18a

def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    return [process_str(x) for x in d]

def process_str(instr):
    return [x for x in instr if x != ' ']

def op(op, num1, num2):
    return num1 + num2 if op == 'add' else num1 * num2

def evaluate(expr):
    total = 0
    curr_op = 'add'

    while expr:
        char = expr.pop(0)
        if char.isdigit():
            num = int(char)
            total = op(curr_op, total, num)
        elif char == '+':
                curr_op = 'add'
        elif char == '*':
                curr_op = 'mult'
        elif char == '(':
            total = op(curr_op, total, evaluate(expr))
        elif char == ')':
            break
    return total

def eval_all(inlist):
    return sum([evaluate(x) for x in inlist])
    
def main():
    print(eval_all(load_data()))

if __name__ == '__main__':
    main()
