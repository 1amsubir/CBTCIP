import random

options = ("rock", "paper", "scissors")

running = True
while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Draw")
    elif player == "paper" and computer == "rock":
        print("You Win")
    elif player == "rock" and computer == "scissors":
        print("You Win")
    elif player == "scissors" and computer == "paper":
        print("You Win")
    else:
        print("You Lose")

    play_again = input("Play again? (y/n): ").lower()
    if play_again == "n":
        running = False
print("Thanks For Playing!")