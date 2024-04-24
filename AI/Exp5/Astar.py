import heapq

def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
def astar(graph, start, goal):
    open_set = [(0, start)]
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    came_from = {}

    while open_set:
        current_f_score, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path
        for neighbor, cost in graph[current_node]:
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    return None
graph = {
(0, 0): [((0, 1), 1), ((1, 0), 1)],
(0, 1): [((0, 0), 1), ((1, 1), 1), ((2, 1), 2)],
(1, 0): [((0, 0), 1), ((1, 1), 1), ((1, 2), 2)],
(1, 1): [((0, 1), 1), ((1, 0), 1), ((1, 2), 1), ((2, 1), 1)], (1, 2): [((1, 1), 1), ((2, 2), 2)],
(2, 1): [((1, 1), 1), ((1, 2), 1), ((2, 2), 1)],
(2, 2): [((1, 2), 2), ((2, 1), 1)]
}
start_node = (0, 0)
goal_node = (2, 2)
path = astar(graph, start_node, goal_node)
if path:
    print("Optimal Path:", ' -> '.join(map(str, path)))
else:
    print("Path not found")