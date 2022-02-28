# AoC 2016 - Day 19a

def calc_winner(total):
    state = list(range(1, total+1))
    while len(state) > 1:
        flag = len(state) % 2 == 1 # last elf hasn't taken a turn.
        step = len(state) // 2
        state = state[::2]
        if flag and len(state) > 1:
            state = state[1:] # ...so take from start of list
            flag = False
    return state[0]

def main():
    print(calc_winner(3004953))

if __name__ == '__main__':
    main()
