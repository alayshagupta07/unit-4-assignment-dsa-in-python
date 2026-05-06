class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

        # Initialize adjacency list
        for i in range(self.V):
            self.graph[i] = []

    # Add directed weighted edge
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    # Print adjacency list
    def print_graph(self):
        print("\nAdjacency List Representation:")
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


# ---------------- MAIN ----------------
if __name__ == "__main__":

    # 6 nodes (0 to 5)
    g = Graph(6)

    # 9 edges (u, v, weight)
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 2),
        (1, 3, 5),
        (2, 3, 7),
        (3, 4, 2),
        (4, 5, 6),
        (5, 0, 1),
        (2, 5, 8)
    ]

    print("Adding edges:")

    for u, v, w in edges:
        print(f"{u} -> {v} (weight {w})")
        g.add_edge(u, v, w)

    # Print final adjacency list
    g.print_graph()