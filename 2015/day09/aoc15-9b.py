# AoC 2015 - Day 9
from parse import parse

class Node:
    def __init__(self, name, near=None):
        self.name = name
        if near is None:
            near = []
        self.near = near

    def __repr__(self):
        return f'{self.name} -> {self.near}'

def load_data():
    graph = []
    with open('input.txt', 'r') as infile:
        for line in infile:
            name, dest, dist = parse('{} to {} = {}', line.strip())
            currnode = find_node(graph, name)
            if not currnode:
                graph.append(Node(name, [(dest, int(dist))]))
            else:
                currnode.near.append((dest, int(dist)))
            destnode = find_node(graph, dest)
            if not destnode:
                graph.append(Node(dest, [(name, int(dist))]))
            else:
                destnode.near.append((name, int(dist)))
    return graph

def find_node(graph, nodename):
    for n in graph:
        if n.name == nodename:
            return n
    return None

def short_path(graph, currloc, visited=[], pathlen=0):
    if len(visited) == len(graph):
        yield (pathlen, visited)
    else:
        currloc = find_node(graph, currloc)
        if not currloc:
            print(currloc)
        for poss in currloc.near:
            if poss[0] not in visited:
                yield from short_path(graph, poss[0], visited + [poss[0]], pathlen + poss[1])

def manager(graph):
    nodes = [x.name for x in graph]
    for n in nodes:
        trips = [x for x in short_path(graph, n, [n])]
        trips = sorted(trips, key = lambda x:x[0], reverse=True)
        print(trips[0])

def main():
    '''
    graph = []
    graph.append(Node('London', [('Dublin', 464), ('Belfast', 518)]))
    graph.append(Node('Belfast', [('Dublin', 141), ('London', 518)]))
    graph.append(Node('Dublin', [('London', 464), ('Belfast', 141)]))
    manager(graph)
    '''
    graph = load_data()
    manager(graph)

if __name__ == '__main__':
    main()
