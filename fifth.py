import math

# Create an empty Tic-Tac-Toe board with 9 positions
board = [' ' for _ in range(9)]


# Function to display the board
def print_board(brd):
    for i in range(3):
        print(f"{brd[3*i]} | {brd[3*i+1]} | {brd[3*i+2]}")
        if i < 2:
            print("--+---+--")


# Function to check whether the given player has won
def is_winner(brd, player):
    wins = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Main diagonal
        [2, 4, 6]   # Secondary diagonal
    ]

    return any(
        all(brd[pos] == player for pos in line)
        for line in wins
    )


# Function to check if the game is a draw
def is_draw(brd):
    return ' ' not in brd


# Function to find all empty positions on the board
def available_moves(brd):
    return [i for i, val in enumerate(brd) if val == ' ']


# Minimax Algorithm
def minimax(brd, is_maximizing):

    # If AI wins, return +1
    if is_winner(brd, 'X'):
        return 1

    # If Human wins, return -1
    if is_winner(brd, 'O'):
        return -1

    # If board is full, return 0 (Draw)
    if is_draw(brd):
        return 0

    # AI's turn (Maximizing player)
    if is_maximizing:
        best_score = -math.inf

        # Try every available move
        for move in available_moves(brd):
            brd[move] = 'X'

            # Recursively evaluate the move
            score = minimax(brd, False)

            # Undo the move
            brd[move] = ' '

            # Choose the maximum score
            best_score = max(best_score, score)

        return best_score

    # Human's turn (Minimizing player)
    else:
        best_score = math.inf

        # Try every available move
        for move in available_moves(brd):
            brd[move] = 'O'

            # Evaluate recursively
            score = minimax(brd, True)

            # Undo the move
            brd[move] = ' '

            # Choose the minimum score
            best_score = min(best_score, score)

        return best_score


# Function to find the best move for AI
def best_move():
    best_score = -math.inf
    move = None

    # Check every possible move
    for i in available_moves(board):

        # AI makes a move
        board[i] = 'X'

        # Find the score using Minimax
        score = minimax(board, False)

        # Undo the move
        board[i] = ' '

        # Store the move with the highest score
        if score > best_score:
            best_score = score
            move = i

    return move


# Main function to play the game
def play():
    print("Tic Tac Toe")
    print("You are 'O' and AI is 'X'")
    print("Board positions are numbered from 0 to 8.\n")

    # Show board positions
    print_board([str(i) for i in range(9)])
    print()

    while True:

        # Human player's turn
        try:
            human_move = int(input("Enter your move (0-8): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Validate the move
        if human_move not in range(9) or board[human_move] != ' ':
            print("Invalid move. Try again.")
            continue

        # Place Human's move
        board[human_move] = 'O'

        print("\nYour Move:")
        print_board(board)

        # Check Human victory
        if is_winner(board, 'O'):
            print("\nCongratulations! You Win.")
            break

        # Check Draw
        if is_draw(board):
            print("\nIt's a Draw.")
            break

        # AI chooses the best move
        ai = best_move()

        # Place AI move
        board[ai] = 'X'

        print("\nAI's Move:")
        print_board(board)

        # Check AI victory
        if is_winner(board, 'X'):
            print("\nAI Wins.")
            break

        # Check Draw
        if is_draw(board):
            print("\nIt's a Draw.")
            break


# Program execution starts here
if __name__ == "__main__":
    play()