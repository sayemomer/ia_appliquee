def alpha_beta_search(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not isinstance(node, list):
        print(f"Evaluating node with value {node}. Alpha: {alpha}, Beta: {beta}")
        return node
    
    if maximizing_player:
        max_eval = float('-inf')
        for child in node:
            eval = alpha_beta_search(child, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                print(f"Pruning branch at node with max_eval {max_eval} due to beta <= alpha. Alpha: {alpha}, Beta: {beta}")
                break
        return max_eval
    
    else:  # Minimizing player
        min_eval = float('inf')
        for child in node:
            eval = alpha_beta_search(child, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                print(f"Pruning branch at node with min_eval {min_eval} due to beta <= alpha. Alpha: {alpha}, Beta: {beta}")
                break
        return min_eval


#main function

if __name__ == "__main__":
    #test the alpha beta search
    tree = [[5, 8], [4, 2], [3, 7]]
    print(alpha_beta_search(tree, 2, float('-inf'), float('inf'), True))