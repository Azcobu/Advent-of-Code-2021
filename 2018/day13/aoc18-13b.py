
def load_data():
    grid, carts = {}, {}
    replace = {'<': '-', '>': '-', '^': '|', 'v': '|'}
    #with open('test-input.txt', 'r') as infile:
    with open('input.txt', 'r') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, char in enumerate(row):
                if char not in [' ', '\n']:
                    if char in replace.keys():
                        grid[(colnum, rownum)] = replace[char]
                        carts[(colnum, rownum)] = (char, 'L')
                    else:
                        grid[(colnum, rownum)] = char
    return grid, carts

def move_cart(grid, carts, cart):
    dir_prims = ['^', '>', 'v', '<']
    dirs = {'^':(0, -1), '>':(1, 0), 'v':(0, 1), '<':(-1, 0)}
    transitions = {('\\', '>'):'v', ('\\', '^'):'<', ('\\', '<'):'^',  ('\\', 'v'):'>',
                   ('/', '^'):'>', ('/', '<'):'v', ('/', '>'):'^', ('/', 'v'):'<'}
    turns = ['L', 'S', 'R']
    cart_x, cart_y = cart[0]
    del carts[(cart_x, cart_y)]
    cart_char, cart_turn = cart[1]
    new_x, new_y = cart_x + dirs[cart_char][0], cart_y + dirs[cart_char][1]

    if (new_x, new_y) in carts: #collision
        print(f'Collision at ({new_x}, {new_y})')
        del carts[(new_x, new_y)]
        return True, (new_x, new_y)

    nextchar = grid[(new_x, new_y)]
    if nextchar in ['-', '|']:
        return False, {(new_x, new_y):cart[1]}
    elif nextchar in ['/', '\\']:
        turnkey = (nextchar, cart_char)
        new_char = transitions[turnkey]
        return False, {(new_x, new_y):(new_char, cart_turn)}
    elif nextchar == '+':
        dirkey = dir_prims.index(cart_char)
        if cart_turn == 'L':
            dirkey -= 1
        elif cart_turn == 'R':
            dirkey += 1
        dirkey = dirkey % 4
        turnkey = (turns.index(cart_turn) + 1) % 3
        new_char = dir_prims[dirkey]
        return False, {(new_x, new_y):(new_char, turns[turnkey])}
        
def sim_carts(grid, carts):
    crash = False
    deleted = []
    
    while len(carts) > 1:
        sorted_carts = sorted(carts.items(), key=lambda x:(x[0][0], x[0][1]))
        deleted = []
        for cart in sorted_carts:
            if cart[0] not in deleted:
                crash, result = move_cart(grid, carts, cart)
                if crash:
                    deleted.append(result)  
                else:
                    carts |= result        
                     
    print(list(carts.items())[0][0])

def main():
    grid, carts = load_data()
    sim_carts(grid, carts)

if __name__ == '__main__':
    main()
