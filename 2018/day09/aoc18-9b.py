# AoC 2018 Day 9a
from collections import defaultdict

class Marble:
    def __init__(self, left, right, num):
        self.left = left
        self.right = right
        self.num = num

def score(numplayers, maxmarble):
    scores = defaultdict(int)
    curr_player = 2

    zero = Marble(None, None, 0)
    one = Marble(zero, zero, 1)
    zero.left = zero.right = one
    curr = one

    for m in range(2, maxmarble + 1):
        if m % 23 != 0:
            newleft = curr.right
            newright = newleft.right
            new = Marble(newleft, newright, m)
            newleft.right = new
            newright.left = new
            curr = new
        else:
            for x in range(7):
                curr = curr.left
            scores[curr_player] += m + curr.num
            curr.left.right = curr.right
            curr.right.left = curr.left
            curr = curr.right

        curr_player = (curr_player + 1) % numplayers
            
    return sorted(scores.items(), key=lambda x:x[1])[-1]
        
def main():
    print(score(405, 7170000))

if __name__ == '__main__':
    main()
