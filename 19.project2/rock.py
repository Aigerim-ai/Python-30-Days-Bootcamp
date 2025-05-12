def determine_winner(player1, player2):
    """Determines the winner of the round."""
    if player1 == player2:
        return "tie"
    elif (player1 == "R" and player2 == "S") or (player1 == "S" and player2 == "P") or (player1 == "P" and player2 == "R"):
        return "player1"
    else:
        return "player2"

def get_player_choice(player_num):
    """Prompts the player for a valid input and returns it."""
    while True:
        choice = input(f"Write R for Rock, P for Paper, S for Scissors Shoot Player {player_num}: ").upper()
        if choice in ['R', 'P', 'S']:
            return choice
        else:
            print("Invalid input, please enter R, P, or S.")

def main():
    iteration = 0
    player_1_score = 0
    player_2_score = 0

    while iteration < 3:
        # Get valid inputs for both players
        player1 = get_player_choice(1)
        player2 = get_player_choice(2)
        
        # Determine round result
        result = determine_winner(player1, player2)
        
        # Update scores based on the result
        if result == "player1":
            player_1_score += 1
        elif result == "player2":
            player_2_score += 1
        
        # Show scores after each round
        print(f"Player 1 Score: {player_1_score}")
        print(f"Player 2 Score: {player_2_score}")

        # End the game if any player reaches 2 points
        if player_1_score == 2 or player_2_score == 2:
            break
        
        iteration += 1

    # Display final game result
    print("\nGame Over!")
    print(f"Player 1 Score: {player_1_score}")
    print(f"Player 2 Score: {player_2_score}")

    if player_1_score > player_2_score:
        print("Player 1 wins!")
    elif player_2_score > player_1_score:
        print("Player 2 wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
