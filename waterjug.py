from collections import deque

MAX_A = 5
MAX_B = 3

def is_goal(state):
    a, b = state
    return a == 1

def get_next_states(state):
    a, b = state
    successors = []

    successors.append((MAX_A, b))
    successors.append((a, MAX_B))
    successors.append((0, b))
    successors.append((a, 0))

    pour = min(a, MAX_B - b)
    successors.append((a - pour, b + pour))

    pour = min(b, MAX_A - a)
    successors.append((a + pour, b - pour))

    return successors

def water_jug_bfs(start_state):
    visited_set = set()
    queue = deque([(start_state, [start_state])])
    visited_set.add(start_state)

    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state):
            return path

        for next_state in get_next_states(current_state):
            if next_state not in visited_set:
                visited_set.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None

def main():
    start_state = (0, 0)

    print(f"Jug A Capacity: {MAX_A} liters")
    print(f"Jug B Capacity: {MAX_B} liters")
    print(f"Initial State: {start_state}")
    print("Goal State: Jug A contains 1 liter -> (1, _)\n")

    solution = water_jug_bfs(start_state)

    if solution:
        print("Solution found! Step-by-step jug contents:\n")
        for step, state in enumerate(solution):
            print(f"Step {step}: Jug A = {state[0]}, Jug B = {state[1]}")
        print(f"\nGoal reached in {len(solution) - 1} steps.")
    else:
        print("No solution found")

if __name__ == "__main__":
    main()