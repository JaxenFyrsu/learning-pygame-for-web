import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    if(player == computer):
        return "It's a tie"
    elif(player == "rock"):
        if(computer == "scissors"):
            return "Player wins"
        else:
            return "Computer wins"
    elif(player == "paper"):
        if(computer == "rock"):
            return "Player wins"
        else:
            return "Computer wins"
    elif(player == "scissors"):
        if(computer == "paper"):
            return "Player wins"
        else:
            return "Computer wins"

game_choices = get_choices()
result = check_win(game_choices["player"], game_choices["computer"])
print("You chose:", game_choices["player"])
print("Computer chose:", game_choices["computer"])
print("Winner is:", result)