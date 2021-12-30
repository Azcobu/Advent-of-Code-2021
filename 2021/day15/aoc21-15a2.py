#AOC 2021 - Day 15

indata = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''

class Node:
    def __init__(self, val, edges={}):
        self.val = val
        self.edges = edges
        self.visited = False

    def add_neighbour(self, neighbour, weight):
        self.edges[neighbour] = weight

    def get_weight(self, neighbour):
        return self.edges[neighbour]

    def __repr__(self):
        return f'{self.val} ({self.edges}) '

#class Graph:

def load_graph(indata):
    graph = {}
    data = indata.splitlines()
    for ypos, row in enumerate(data):
        for xpos, val in enumerate(row):
            newnode = Node(val)
            for yshift, xshift in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if 0 <= ypos + yshift < len(data) and\
                   0 <= xpos + xshift < len(row):
                    nval = data[ypos+yshift][xpos+xshift]
                    newnode.add_neighbour((ypos+yshift, xpos+xshift), nval)
            graph[(ypos, xpos)] = newnode
    return graph

def main():
    g = load_graph(indata)
    print(g[(1, 1)])
    #print(g)

if __name__ == '__main__':
    main()
