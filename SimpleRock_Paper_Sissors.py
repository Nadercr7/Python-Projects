import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    # Get player's choice
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # Validate player's input
    if player_choice not in choices:
        print("Invalid choice! Please try again.")
        return
    
    # Get computer's random choice
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# Start the game
play_game()
