from graph_input import read_graph

def choose_node(reachable, explored):
    for node in reachable:
        if node not in explored:
            return node

def find_path(start_node, goal_node, graph):
    reachable = [start_node]
    explored = set()
    previous = {start_node: None}
    while len(reachable) > 0:
        cur_node = choose_node(reachable, explored)
        if cur_node == goal_node:
            return build_path(goal_node, previous)
        reachable.remove(cur_node)
        explored.add(cur_node)
        new_reachable = graph[cur_node] - explored
        for adjacent in new_reachable:
            if adjacent not in reachable:
                previous[adjacent] = cur_node
                reachable.append(adjacent)
                
def build_path(to_node, previous_nodes):
    path = []
    while to_node != None:
        path.append(to_node)
        to_node = previous_nodes[to_node]
    return path

def main():
    graph = read_graph('sample_data/sample_1.txt')
    path = find_path('A', 'T', graph)
    print path

if __name__ == '__main__':
    main()