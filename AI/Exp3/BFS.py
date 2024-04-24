from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        print(f"Visited node {node} with path: {' -> '.join(path)}")

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C']
}

start_node = 'A'
goal_node = 'F'
print(f"Starting BFS from node {start_node} to find node {goal_node}:")

path = bfs(graph, start_node, goal_node)

if path:
    print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")
