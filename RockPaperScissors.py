import random

print("--------Welcome to RPS, let the game begin--------")

# creating player choice


def player_choice():
    player = input("You choose  Rock , Paper , Scissors? ")
    # making a list toe see if the input the player made is in the list to execute the correct if statement
    if player in ["Rock", "rock"]:
        player = "Rock"

    elif player in ["Paper", "paper"]:
        player = "Paper"

    elif player in ["Scissors", "scissors"]:
        player = "Scissors"

    else:
        print("That's not a valid play. Invalid Option!") # error message
        player_choice()
    return player

# Creating the computer


def computer_move():
    computer_choice = random.randint(1, 3)  # generator
    if computer_choice == 1:
        computer_choice = "Rock"
    elif computer_choice == 2:
        computer_choice = "Paper"
    else:
        computer_choice = "Scissors"
    return computer_choice


# Looping the Functions with a While True:
while True:
    print("")
    player = player_choice()
    computer_choice = computer_move()
    if player == "Rock":
        if computer_choice == "Rock":
            print("Tie")
        elif computer_choice == "Paper":
            print("You lose! Paper covers Rock. ")
        elif computer_choice == "Scissors":
            print("You win! Rock smashes Scissors. ")
    elif player == "Paper":
        if computer_choice == "Paper":
            print("Tie!")
        elif computer_choice == "Scissors":
            print("You lose! Scissors cuts Paper. ")
        elif computer_choice == "Rock":
            print("You win! Paper covers Rock. ")
    elif player == "Scissors":
        if computer_choice == "Scissors":
            print("Tie")
        elif computer_choice == "Rock":
            print("You lose! Rock smashes Scissors. ")
        elif computer_choice == "Paper":
            print("You win! Scissors cuts Paper. ")
    user_choise = input("Do you want to play again? (y / n)  ")
    if user_choise.capitalize() == "Y":
        pass
    elif user_choise.capitalize() == "N":
        break
    else:
        break
