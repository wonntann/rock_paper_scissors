# import random module
import random

# intro
print("Rock, Paper, Scissors...")

# main function
def main():
  # Random Choice (Rock, Paper, or Scissors)
    rps = ["Rock", "Paper", "Scissors"]
    computer = random.choice(rps)

  # player's choice
    player = input("your choice: ").capitalize()

  # tie
    if player == computer:
        print("Tie!")

  # if the player selects rock
    elif player == "Rock":
    	# if the computer selects paper
        if computer =="Paper":
            print("You lose!", computer, "covers", player)
        # if the computer selects scissors
        else:
            print("You win!", player, "smashes", computer)
            

  # if the player selects paper
    elif player == "Paper":
    	# if the computer selects rock
        if computer =="Rock":
            print("You win!", player, "covers", computer)
        # if the computer selects scissors
        else:
            print("You lose!", computer, "cuts", player)

  # if the player selects scissors
    elif player == "Scissors":
    	# if the computer selects rock
        if computer =="Rock":
            print("You lose...", computer, "smashes", player)
        # if the computer selects paper
        else:
            print("You win!", player, "cuts", computer)
  # if the computer wants to play again
    play_again = input("Do you want to play again? yes or no: ").lower().capitalize()
    # if the computer says yes, go back to the function
    if play_again == "Yes":
        main()
    # if the computer says no, say goodbye
    elif play_again == "No":
        print("Goodbye")

# end of function
main()