# Tic-Tac-Toe board representation:
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

def evaluate_board(board):
    # This function evaluates the current board state.
    # It returns +1 if the maximizing player wins, -1 if the minimizing player wins, or 0 for a draw.
    
    # Define winning combinations (rows, columns, diagonals)
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c]:
            if board[a] == 'X':
                return 1  # Maximizing player (X) wins
            elif board[a] == 'O':
                return -1  # Minimizing player (O) wins
    
    if ' ' not in board:
        return 0  # It's a draw
    
    return None  # The game is still ongoing

def minimax(board, depth, maximizingPlayer):
    # Minimax algorithm for Tic-Tac-Toe
    # board: current game board represented as a list
    # depth: current depth in the game tree
    # maximizingPlayer: True for X (Max), False for O (Min)

    # Base cases: game over or maximum depth reached
    result = evaluate_board(board)
    if result is not None:
        return result * depth  # Apply depth to favor shorter wins
       
    if maximizingPlayer:
        max_eval = -float('inf')
        best_move = None

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                if eval > max_eval:
                    max_eval = eval
                    best_move = i

        if depth == 0:
            return best_move  # Return the best move for the root
        else:
            return max_eval  # Return the evaluation value for this level

    else:
        min_eval = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)

        return min_eval

def make_best_move(board):
    # Find the best move using the minimax algorithm
    best_move = minimax(board, 0, True)
    board[best_move] = 'X'

# Initialize an empty Tic-Tac-Toe board
board = [' '] * 9

while True:
    make_best_move(board)
    print(f"Player X's move:")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

    result = evaluate_board(board)
    if result == 1:
        print("Player X wins!")
        break
    elif result == 0:
        print("It's a draw!")
        break

    # Player O's move (You can implement a real player here)
    while True:
        move = int(input("Enter your move (0-8): "))
        if board[move] == ' ':
            board[move] = 'O'
            break

    print(f"Player O's move:")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

    result = evaluate_board(board)
    if result == -1:
        print("Player O wins!")
        break
    elif result == 0:
        print("It's a draw!")
        break
