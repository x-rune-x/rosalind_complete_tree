class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges


def create_graph(file_path):
    with open(file_path) as file:
        n = int(file.readline())
        edges = []
        for line in file:
            raw_edge = line.split(' ')
            edge = [node.strip() for node in raw_edge]
            edges.append(edge)

        return Graph(n, edges)


new_graph = create_graph('sample.txt')
expected_edges = new_graph.nodes - 1
edges_to_add = expected_edges - len(new_graph.edges)
print(edges_to_add)
