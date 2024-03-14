def a_star(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        n = min(open_set, key=lambda x: g.get(x, float('inf')) + heuristic(x))
        if n == stop_node or not Graph_nodes[n]:
            break

        for m, weight in get_neighbors(n) or []:
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m], g[m] = n, g[n] + weight
            elif g[m] > g[n] + weight:
                g[m], parents[m] = g[n] + weight, n
                if m in closed_set:
                    closed_set.remove(m)
                    open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    if n != stop_node:
        print('Path does not exist!')
        return None

    path = [stop_node]
    while parents[n] != n:
        path.append(parents[n])
        n = parents[n]
    path.append(start_node)
    path.reverse()

    print('Path found:', path)
    return path

def get_neighbors(v):
    return Graph_nodes.get(v, [])

def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist.get(n, float('inf'))

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

a_star('A', 'G')
