from queue import PriorityQueue

# Define the graph as an adjacency list with costs
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 6)],
    'D': [('G', 2)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values (estimated cost to goal 'G')
heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 4,
    'G': 0
}


def a_star_search(graph, start, goal):
    # Priority queue stores:
    # (f_score, current_node, path, g_score)
    pq = PriorityQueue()

    # f = g + h
    pq.put((heuristics[start], start, [start], 0))

    visited = set()

    while not pq.empty():
        f, current, path, g = pq.get()

        if current in visited:
            continue

        visited.add(current)

        # Check if goal is reached
        if current == goal:
            print("Path found:", ' -> '.join(path))
            print("Total cost:", g)
            return

        # Explore neighbors
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]

                pq.put(
                    (new_f, neighbor, path + [neighbor], new_g)
                )

    print("No path found from", start, "to", goal)


# Run the A* Search
start_node = 'A'
goal_node = 'G'

print("A* Search from", start_node, "to", goal_node)
a_star_search(graph, start_node, goal_node)