# AoC 2017 - Day 7b - hlhomy

class Program:
    def __init__(self, name, wght, children=None):
        self.name = name
        self.wght = wght
        if children != None:
            self.children = []
        else:
            self.children = None

    def __repr__(self):
        return f'{self.name} ({self.wght}) {self.children}'

def load_data():
    nodes = []
    with open('input.txt', 'r') as infile:
        d = [x.split() for x in infile]

    root = 'hlhomy'
    for node in d:
        name = node[0]
        wght = int(node[1][1:-1])
        chil = node[3:] if len(node) > 2 else None
        nodes.append(Program(name, wght, chil))

    return nodes

def main():
    print(load_data())

if __name__ == "__main__":
    main()
