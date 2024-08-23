def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = (
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    )
    return [player, player, player] in win_conditions

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken, try again.")
    
    print_board(board)
    print("It's a draw!")

tic_tac_toe()
