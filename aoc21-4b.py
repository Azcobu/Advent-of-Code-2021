#Advent of Code 2021 - 4b

def load_data(fname):
    boardlist = []
    with open(fname, 'r') as indata:
        numbers = [int(x.strip()) for x in indata.readline().split(',')]
        boards = [x.strip() for x in indata.readlines() if x not in  ['\n', ' ']]
        for b in range(len(boards)//5):
            newboard = []
            for line in boards[b*5:(b+1)*5]:
                newboard.append([int(x) for x in line.split() if x])
            boardlist.append(newboard)
    return numbers, boardlist

def check_numbers(nums, boards):
    wonboards = []
    win_num = 0
    for pos, num in enumerate(nums):
        numset = set(nums[:pos+1])
        for boardnum, board in enumerate(boards):
            for line in board: # rows
                if len(set(line) & numset) == 5:
                    if boardnum not in wonboards:
                        wonboards.append(boardnum)
                        win_num = num
            for colnum in range(5):
                col = [x[colnum] for x in board]
                if len(set(col) & numset) == 5:
                    if boardnum not in wonboards:
                        wonboards.append(boardnum)
                        win_num = num
    return wonboards, win_num

def sum_board(board, nums, win_num):
    total = 0
    numset = nums[:nums.index(win_num)+1]
    for line in board:
        for item in line:
            if item not in numset:
                total += item
    return total

def main():
    #nums, boards = load_data(r'D:\Python\Code\aoc21\aoc-4-test.txt')
    nums, boards = load_data(r'D:\Python\Code\aoc21\aoc-4-input.txt')
    wonboards, win_num = check_numbers(nums, boards)
    lastwon = wonboards[-1]
    boardsum = sum_board(boards[lastwon], nums, win_num)
    print(boardsum * win_num )
    #assert boardsum * win_num == 4512


if __name__ == '__main__':
    main()
