import random

# Tic-Tac-Toe board as a 2D list
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
def display_board():
    for row in board:
        print(" , ".join(row))
    print()

def user_move():
    print("Your Turn (X).")
    while True:
        try:
            row = int(input("Choose row (0-2): "))
            col = int(input("Choose column (0-2): "))
            if row in range(3) and col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("That spot is already taken.")
            else:
                print("Enter numbers between 0 and 2.")
        except ValueError:
            print("Please enter valid numbers.")

def computer_move():
    print("Computer's turn (O).")
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
turn = 0
while turn < 9:
    display_board()
    if turn % 2 == 0:
        user_move()
    else:
        computer_move()
    turn += 1

display_board()
print("Game over!")        