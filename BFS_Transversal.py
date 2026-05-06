from collections import deque

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque()
    result = []

    # Start BFS
    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)

        # Visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# ---------------- MAIN ----------------
if __name__ == "__main__":

    # Adjacency list (Directed graph)
    graph = {
        0: [1, 2],
        1: [2, 3],
        2: [3, 5],
        3: [4],
        4: [],
        5: [0]
    }

    start_node = 0

    print("Graph Adjacency List:")
    for k in graph:
        print(k, "->", graph[k])

    print("\nBFS Traversal starting from node", start_node)

    bfs_result = bfs(graph, start_node)

    print("BFS Order:", bfs_result)