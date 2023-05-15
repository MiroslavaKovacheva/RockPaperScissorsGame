import random

while True:
    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    player_move = input("Choose rock, paper or scissors: ")

    if player_move == "rock":
        player_move = rock
    elif player_move == "paper":
        player_move = paper
    elif player_move == "scissors":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer chose {computer_move}!")

    if player_move == computer_move:
        print(f"Since you both selected {player_move}, it's a tie!")
    elif player_move == rock:
        if computer_move == scissors:
            print("Rock smashes scissors! You win!")
        elif computer_move == paper:
            print("Paper covers rock! You lose.")
    elif player_move == paper:
        if computer_move == scissors:
            print("Scissors cuts paper! You lose.")
        elif computer_move == rock:
            print("Paper covers rock! You lose.")
    elif player_move == scissors:
        if computer_move == paper:
            print("Scissors cuts paper! You win.")
        elif computer_move == rock:
            print("Rock smashes scissors! You lose!")

    print()
    play_again = input("Do you want to try again? (Yes / No): ")

    if play_again.lower() != "yes":
        break
