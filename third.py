from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Depth First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=' ')
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Breadth First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)

            queue.extend(
                [node for node in graph[vertex] if node not in visited]
            )


# Main Program Execution
print("Depth First Search (DFS) starting from vertex 'A':")
dfs(graph, 'A')

print("\n")

print("Breadth First Search (BFS) starting from vertex 'A':")
bfs(graph, 'A')