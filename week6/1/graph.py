class DirectedGraph:

    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return str(self.graph)

    def add_edge(self, node_a, node_b):
        if node_a not in self.graph.keys():
            self.graph[node_a] = [node_b]
        elif node_b not in self.graph[node_a]:
            self.graph[node_a].append(node_b)
        if node_b not in self.graph.keys():
            self.graph[node_b] = []

    def get_neighbors_for(self, node):
        return self.graph[node]

    def path_between(self, node_a, node_b):
        queue = [node_a]
        while queue != []:
            for node in self.graph[queue[0]]:
                if node == node_b:
                    return True
                queue.append(node)
            queue.pop(0)
        return False
