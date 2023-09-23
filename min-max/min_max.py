import math

def evaluate(node):
    # In this simple example, the evaluation function returns the difference
    # between the sums of numbers chosen by Max and Min.
    return sum(node)  # The current node is represented as a list of numbers.

def minimax(node, depth, maximizingPlayer):
    if depth == 0:
        return evaluate(node), None

    if maximizingPlayer:
        maxEval = -math.inf
        bestMove = None
        for i, value in enumerate(node):
            if value is None:
                continue
            child_node = list(node)  # Create a copy of the current node
            child_node[i] = None     # Mark the chosen number as None
            eval, _ = minimax(child_node, depth - 1, False)
            if eval > maxEval:
                maxEval = eval
                bestMove = i  # Store the index of the chosen number as the move
        return maxEval, bestMove
    else:
        minEval = math.inf
        bestMove = None
        for i, value in enumerate(node):
            if value is None:
                continue
            child_node = list(node)
            child_node[i] = None
            eval, _ = minimax(child_node, depth - 1, True)
            if eval < minEval:
                minEval = eval
                bestMove = i
        return minEval, bestMove

# Example usage:
initial_state = [3, 5, 2, 9, 7]  # Initial game state (a list of numbers)
depth = 3  # Set the depth of the search tree (you can adjust this)

best_eval, best_move = minimax(initial_state, depth, True)

print("Best Move:", best_move)
print("Best Evaluation Value:", best_eval)
