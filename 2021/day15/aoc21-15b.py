#AOC 2021 - Day 15

from queue import PriorityQueue

def load_data(fname='input.txt'):
    graph = {}
    with open(fname, 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    for ypos, row in enumerate(data):
        for xpos, val in enumerate(row):
            graph[(xpos, ypos)] = int(val)
    graph['sizes'] = (xpos + 1, ypos + 1)
    return graph

def calc_cost(graph, x, y, tiles):
    x_rpt, xpos = divmod(x, graph['sizes'][0])
    y_rpt, ypos = divmod(y, graph['sizes'][1])
    val = graph[(xpos, ypos)] + x_rpt + y_rpt
    if val > 9:
        val = val % 10 + 1
    return val

def navigate(graph, tiles):
    size_x = (max(x[0] for x in graph.keys() if x != 'sizes') + 1) * tiles
    size_y = (max(y[1] for y in graph.keys() if y != 'sizes') + 1) * tiles
    visited = {(x, y): float('inf') for x in range(size_x) for y in range(size_y)}
    graph['target'] = (size_x - 1, size_y - 1)
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
                new_cost = cost + calc_cost(graph, new_x, new_y, tiles)
                if new_cost < old_cost:
                    unvisit.put((new_cost, (new_x, new_y)))
                    visited[(new_x, new_y)] = new_cost
  
    return visited[graph['target']]

def main():
    assert navigate(load_data('example.txt'), 5) == 315
    print(navigate(load_data(), 5))

if __name__ == '__main__':
    main()
