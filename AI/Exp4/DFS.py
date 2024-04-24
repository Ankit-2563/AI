def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        current_node, path = stack.pop()
        print("Visiting node:", current_node, "Path:", ' -> '.join(path))
        if current_node == goal:
            print("Goal node reached!")
            return
        visited.add(current_node)
        for neighbor in reversed(graph[current_node]):
            if neighbor not in visited and neighbor not in (node for node, _ in stack):
                stack.append((neighbor, path + [neighbor]))
    print("Goal node not reachable!")
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
'F': ['C'] }
start_node = 'A'
goal_node = 'F'
print("Starting DFS from node:", start_node)
dfs(graph, start_node, goal_node)