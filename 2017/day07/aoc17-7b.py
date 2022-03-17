# AoC 2017 - Day 7b - hlhomy
from statistics import median

class Program:
    def __init__(self, name, wght, children=None):
        self.name = name
        self.wght = wght
        if children != None:
            self.children = children
        else:
            self.children = []

    def __repr__(self):
        return f'{self.name} ({self.wght}) {self.children}'

def load_data():
    nodes = []
    with open('input.txt', 'r') as infile:
        for line in infile:
            k = [x.strip(', ') for x in line.split()]
            p = Program(k[0], int(k[1][1:-1]))
            if len(k) > 2:
                p.children = k[3:]
            nodes.append(p)
    return nodes

def build_tree(data, node):
    if not node.children:
        return node
    else:
        kids = [x for x in data if x.name in node.children]
        for k in kids:
            node.children.remove(k.name)
            node.children += [(build_tree(data, k))]
    return node

def calc_weights(node):
    if not node.children:
        return node.wght
    else:
        return node.wght + sum([calc_weights(x) for x in node.children])

def find_unbalanced_child(node):
    wghts = {c:calc_weights(c) for c in node.children}
    if len(set(wghts.values())) > 1:
        outlier = [x for x in wghts.values() if x != median(wghts.values())][0]
        if outlier:
            for k, v in wghts.items():
                if v != median(wghts.values()):
                    print(f'{k.name} unbalanced with weight of {v} - median is { median(wghts.values())}')
                    offset = abs(median(wghts.values()) - v)
                    return k, offset
    else:
        return None, None

def seek(node):
    wrong = []
    c, offset = find_unbalanced_child(node)
    while c:
        wrong.append(c)
        c, o = find_unbalanced_child(c)
    found = wrong[-1]
    return found.wght - offset

def main():
    d = load_data()
    root = Program('hlhomy', 30, [])
    root.children += ['oylgfzb', 'ahayh', 'razvskj', 'hvtvcpz', 'teyrfjn', 'lqirhg', 'dxxty']
    tree = build_tree(d, root)
    print(seek(tree))
    #print(find_unbalanced_child)

if __name__ == "__main__":
    main()
