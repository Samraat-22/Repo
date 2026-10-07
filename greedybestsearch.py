
import heapq

adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic_values = {
    'A': 5,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 1,
    'F': 0
}

def greedy_best_first_search(adj_list, heuristic_values, start, goal):
    visitd = set()
    priority_queue = [(heuristic_values[start], start,[start])]
    
    while priority_queue:
        h_value, current_node,path = heapq.heappop(priority_queue)
        if current_node in visitd:
            continue
        visitd.add(current_node)
        
        if current_node == goal:
            print("found goal")
            return path
            
        for neighbour in adj_list[current_node]:
            if neighbour not in visitd:
                heapq.heappush(priority_queue, (heuristic_values[neighbour], neighbour,path+[neighbour]))
                print("goal node could be reached")
    return None


start_node = 'A'
goal_node = 'F'
result = greedy_best_first_search(adj_list, heuristic_values, start_node, goal_node)
print(f"Initial State: {start_node}")
print(f"Goal State: {goal_node}")
print(f"Path Found by Greedy Best-First Search: {result}")
