import random

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("\n  0   1   2")
    for idx, row in enumerate(board):
        print(f"{idx} " + " | ".join(row))
        if idx < 2:
            print("  ---------")
    print()

def is_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def user_move(board):
    print("Your Turn (X)")
    while True:
        try:
            row = int(input("Choose row (0-2): "))
            col = int(input("Choose column (0-2): "))
            if row in range(3) and col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    return
                else:
                    print("❌ That spot is already taken.")
            else:
                print("⚠️ Enter numbers between 0 and 2.")
        except ValueError:
            print("⚠️ Please enter valid numbers.")

def computer_move(board):
    print("Computer's Turn (O)")
    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    if empty:
        row, col = random.choice(empty)
        board[row][col] = 'O'

def play_game():
    board = create_board()
    current_player = 'X'

    while True:
        display_board(board)

        if current_player == 'X':
            user_move(board)
        else:
            computer_move(board)

        if is_winner(board, current_player):
            display_board(board)
            print(f"🎉 {current_player} wins!")
            break

        if is_draw(board):
            display_board(board)
            print("🤝 It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    print("🎮 Welcome to Tic-Tac-Toe!")
    play_game()
