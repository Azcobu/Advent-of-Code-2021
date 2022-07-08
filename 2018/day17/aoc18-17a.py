from parse import parse

def load_data():
    clay = set()
    with open('test-input.txt', 'r') as infile:
        indata = [x.strip() for x in infile.readlines()]

    parsestr = '{}={}, {}={}..{}'
    for line in indata:
        p1, p1num, p2, p2num1, p2num2 = parse(parsestr, line)
        p1num, p2num1, p2num2 = int(p1num), int(p2num1), int(p2num2)

        if p1 == 'x':
            for ynum in range(p2num1, p2num2+1):
                clay.add((p1num, ynum))
        else:
            for xnum in range(p2num1, p2num2+1):
                clay.add((xnum, p1num))
    return clay

def sim_flow(clay, water):
    flowing, stable = set(), set()
    flowing.add(water)

    clay_y = {y[1] for y in clay}
    min_y, max_y = min(clay_y), max(clay_y)

    print_grid(clay, flowing, stable)

    for x in range(20):
        not_empty = clay | flowing | stable
        newflow = set()
        for stream in flowing:
            left, under, right = (stream[0]-1, stream[1]), (stream[0], stream[1]+1), (stream[0]+1, stream[1])
            if under not in not_empty:
                newflow.add(under)
                #stable.add(stream)
            if under in clay or under in stable or under in flowing:
                newflow.add(stream)
                if left not in not_empty:
                    newflow.add(left)
                if right not in not_empty:
                    newflow.add(right)
        flowing = newflow
        print_grid(clay, flowing, stable)

def print_grid(clay, flowing, stable):
    state = clay | flowing | stable
    state_x = {x[0] for x in state}
    state_y = {y[1] for y in state}
    min_x, max_x = min(state_x), max(state_x)
    min_y, max_y = min(state_y), max(state_y)

    for ypos in range(min_y, max_y + 1):
        for xpos in range(min_x, max_x + 1):
            char = ''
            if (xpos, ypos) in clay:
                char ='#'
            elif (xpos, ypos) in stable:
                char = '~'
            elif  (xpos, ypos) in flowing:
                char = '|'
            else:
                char = '.'
            print(char, end='')
        print()
    print()

def main():
    water = (500, 0)
    sim_flow(load_data(), water)

if __name__ == '__main__':
    main()
