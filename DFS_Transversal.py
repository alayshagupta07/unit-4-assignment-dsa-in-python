def dfs(graph, node, visited, result):
    visited.add(node)
    result.append(node)

    # Visit all neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)


# ---------------- MAIN ----------------
if __name__ == "__main__":

    # Adjacency list (Directed graph)
    graph = {
        0: [1, 2],
        1: [3],
        2: [3, 5],
        3: [4],
        4: [],
        5: [0]
    }

    start_node = 0

    print("Graph Adjacency List:")
    for k in graph:
        print(k, "->", graph[k])

    visited = set()
    result = []

    print("\nDFS Traversal starting from node", start_node)

    dfs(graph, start_node, visited, result)

    print("DFS Order:", result)