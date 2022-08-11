#AOC 2021 - Day 15

from queue import PriorityQueue

def load_graph():
    graph = {}
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]

    for ypos, row in enumerate(data):
        for xpos, val in enumerate(row):
            graph[(xpos, ypos)] = int(val)
    graph['target'] = (xpos, ypos)
    return graph

def navigate(graph):
    visited = {k: float('inf') for k in graph.keys()}
    visited[(0, 0)] = 0

    unvisit = PriorityQueue()
    unvisit.put((0, (0, 0)))

    while not unvisit.empty():
        (cost, curr_node) = unvisit.get()
        visited[(curr_node)] = cost

        for d_x, d_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = curr_node[0] + d_x, curr_node[1] + d_y
            if 0 <= new_x <= graph['target'][0] and 0 <= new_y <= graph['target'][1]:
                old_cost = visited[(new_x, new_y)]
                new_cost = cost + graph[(new_x, new_y)]
                if new_cost < old_cost:
                    unvisit.put((new_cost, (new_x, new_y)))
                    visited[(new_x, new_y)] = new_cost
  
    return visited[graph['target']]

def main():
    g = load_graph()
    print(navigate(g))

if __name__ == '__main__':
    main()
