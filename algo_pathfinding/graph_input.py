def read_graph(path_file):
    graph = {}
    with open(path_file, 'r') as f:
        data = f.read()
        graph_data = eval(data)
    return graph_data