import math

values = [3, 5, 4, 5]
max_depth = int(math.log2(len(values)))

def minimax(depth, node_index, is_maximizing_player, values, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_maximizing_player:
        left_score = minimax(depth + 1, node_index * 2, False, values, max_depth)
        right_score = minimax(depth + 1, node_index * 2 + 1, False, values, max_depth)
        return max(left_score, right_score)
    else:
        left_score = minimax(depth + 1, node_index * 2, True, values, max_depth)
        right_score = minimax(depth + 1, node_index * 2 + 1, True, values, max_depth)
        return min(left_score, right_score)

def main():
    print(f"Leaf values: {values}")
    print(f"Max depth: {max_depth}")

    optimal_value = minimax(0, 0, True, values, max_depth)

    print(f"\nThe optimal value is: {optimal_value}")

if __name__ == "__main__":
    main()