#Rock,Paper,Scissors Project
# player1=(input("Write R for Rock, P for Paper , S for Scissors Shoot Player 1 "))
# player2=(input("Write R for Rock, P for Paper , S for Scissors Shoot Player 2 "))


Iteration=0
Player_1_Score=0
Player_2_Score=0

while Iteration < 3:
    player1=(input("Write R for Rock, P for Paper , S for Scissors Shoot Player 1 "))
    player2=(input("Write R for Rock, P for Paper , S for Scissors Shoot Player 2 "))
    
    
    if player1==player2:
        print("It's a tie Try Again")
        continue
    if player1=="R" and player2=="S":
        Player_1_Score+=1
    if player1=="S" and player2=="R":
        Player_2_Score+=1   
    if player1=="S" and player2=="P":
        Player_1_Score+=1  
    if player1=="P" and player2=="S":
        Player_2_Score+=1   
    if player1=="P" and player2=="R":
        Player_1_Score+=1 
    if player1=="R" and player2=="P":
        Player_2_Score+=1        
    print(f"Player 1 Score: {Player_1_Score}")
    print(f"Player 2 Score: {Player_2_Score}")

    Iteration += 1     

    if Player_1_Score == 2 or Player_2_Score == 2:
        break      

print("\nGame Over!")
print(f"Player 1 Score: {Player_1_Score}")
print(f"Player 2 Score: {Player_2_Score}")

if Player_1_Score > Player_2_Score:
    print("Player 1 wins!")
elif Player_2_Score > Player_1_Score:
    print("Player 2 wins!")
else:
    print("It's a draw!")