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
        for line in infile:
            k = line.split()
            p = Program(k[0], int(k[1][1:-1]))
            if len(k) > 2:
                p.children = k[3:]
            nodes.append(p)
    return nodes

def build_tree(data, node):
    if not node.children:
        return node
    else:
        for x in node.children:
            for x in data:
                if node.children and x.name in node.children:
                    node.children.remove(x.name)
                    node.children += [(build_tree(data, x))]
                    return node

def main():
    d = load_data()
    root = Program('hlhomy', 30, 'a')
    root.children += ['oylgfzb,', 'ahayh,', 'razvskj,', 'hvtvcpz,', 'teyrfjn,', 'lqirhg,', 'dxxty']
    tree = build_tree(d, root)
    print(tree)


if __name__ == "__main__":
    main()
