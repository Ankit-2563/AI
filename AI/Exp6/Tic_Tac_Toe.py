import random
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
def check_winner(board, player):
    winning_combinations = [
    [0,1,2],[3,4,5],[6,7,8], #Rows 
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns 
    [0, 4, 8], [2, 4, 6] # Diagonals
]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False
def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]
def ai_move(board):
    return random.choice(available_moves(board))
def tic_tac_toe():
    board = [" " for _ in range(9)]
    players = ["X", "O"]
    current_player = players[random.randint(0, 1)]
    print("Let's play Tic Tac Toe!") 
    print_board(board)
    while True:
        print(f"Player {current_player}'s turn.")
        if current_player == "X":
            move = int(input("Enter cell number (1-9): ")) - 1
            if board[move] != " ":
                print("Cell already taken. Try again.")
                continue
        else:
            move = ai_move(board)
        board[move] = current_player
        print_board(board)
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif " " not in board:
            print("It's a draw!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]
tic_tac_toe()