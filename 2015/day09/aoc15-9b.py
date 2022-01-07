# AoC 2015 - Day 9
from parse import parse

def load_data():
    graph = {}
    with open('input.txt', 'r') as infile:
        for line in infile:
            name, dest, dist = parse('{} to {} = {}', line.strip())
            if name not in graph:
                graph[name] = {}
            graph[name][dest] = int(dist)
            if dest not in graph:
                graph[dest] = {}
            graph[dest][name] = int(dist)
    return graph

def short_path(graph, currloc, visited=[], pathlen=0):
    if len(visited) == len(graph):
        yield (pathlen, visited)
    else:
        for poss in graph[currloc].keys():
            if poss not in visited:
                yield from short_path(graph, poss, visited + [poss], pathlen + graph[currloc][poss])

def manager(graph):
    mintrips = []
    for n in graph.keys():
        trips = [x for x in short_path(graph, n, [n])]
        trips = sorted(trips, key = lambda x:x[0], reverse=True)
        mintrips.append(trips[0])
    print(sorted(mintrips)[-1])

def main():
    graph = load_data()
    manager(graph)

if __name__ == '__main__':
    main()
