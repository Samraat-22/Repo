import heapq

graph = {
    'A': [('B', 1), ('C', 4), ('D', 3)],
    'B': [('E', 2)],
    'C': [('E', 1), ('F', 5)],
    'D': [('F', 6)],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0
}

def a_star_search(start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current_node, path = heapq.heappop(open_set)

        if current_node == goal:
            return path, g

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

def main():
    print("Graph adjacency list with costs:")
    for node in graph:
        print(f"{node} -> {graph[node]}")

    print("\nHeuristic values:")
    for node in heuristic:
        print(f"h({node}) = {heuristic[node]}")

    start_node = 'A'
    goal_node = 'F'

    result_path, total_cost = a_star_search(start_node, goal_node)

    print(f"\nStart Node: {start_node}")
    print(f"Goal Node: {goal_node}")

    if result_path:
        print(f"Path found: {' -> '.join(result_path)}")
        print(f"Total cost: {total_cost}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()