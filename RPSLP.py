import random

computer = 0
player = 0

while True:
    print("\nYou will be playing a game of Rock Paper Scissors Lizard Spock inspired by The Big Bang Theory")
    print("Score will be kept in [wins, ties, losses] for this game")

    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    win = 0
    tie = 0
    lose = 0
    score = [win, tie, lose]  # score per round

    while True:
        try:
            rounds = int(input("\nType the number of rounds you want to play: "))
            if rounds <= 0:
                print("Not a valid number.")
                continue
            elif rounds > 50:
                print("Keep the number under 50.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
            continue

    # rounds per loop
    for i in range(rounds):
        player_choice = input("\nPick rock, paper, scissors, lizard, or spock: ").lower()
        if player_choice not in choices:
            print("That's not a valid choice. Try again!\n")
            continue

        computer_choice = random.choice(choices)
        print("You chose:", player_choice, " Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
            tie += 1
        elif (player_choice == "rock" and computer_choice in ["scissors", "lizard"]) or \
             (player_choice == "scissors" and computer_choice in ["paper", "lizard"]) or \
             (player_choice == "paper" and computer_choice in ["rock", "spock"]) or \
             (player_choice == "spock" and computer_choice in ["rock", "scissors"]) or \
             (player_choice == "lizard" and computer_choice in ["paper", "spock"]):
            print("You won!")
            win += 1
        else:
            print("Computer wins :(")
            lose += 1

        score = [win, tie, lose]
        print("Round score:", score)

    # when there's a tie
    while win == lose:
        print("\nTie breaker round! Play one more round to determine a winner.\n")
        player_choice = input("Pick rock, paper, scissors, lizard, or spock: ").lower()
        if player_choice not in choices:
            print("That's not a valid choice. Try again!\n")
            continue

        computer_choice = random.choice(choices)
        print("You chose:", player_choice, " Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
            tie += 1
        elif (player_choice == "rock" and computer_choice in ["scissors", "lizard"]) or \
             (player_choice == "scissors" and computer_choice in ["paper", "lizard"]) or \
             (player_choice == "paper" and computer_choice in ["rock", "spock"]) or \
             (player_choice == "spock" and computer_choice in ["rock", "scissors"]) or \
             (player_choice == "lizard" and computer_choice in ["paper", "spock"]):
            print("You won!")
            win += 1
        else:
            print("Computer wins :(")
            lose += 1

        score = [win, tie, lose]
        print("Round score:", score)

    # game ends
    if win > lose:
        print("\nGame over,  you win!")
        player += 1
    else:
        print("\nGame over, you lose :(")
        computer += 1

    print("The overall game score (player:computer) is", [player, computer])

    play_again = input("\nWould you like to play again? (yes/no) ").lower()
    if play_again != "yes":
        if player > computer:
            print(f"you won overall with {player} wins!")
        elif player < computer:
            print(f"You lost overall with {player} wins and the computer had {computer} wins")
        else:
            print("There is a tie. no one wins")
        print("Thanks for playing! Bye :)")
        break
