from random import randint

#create a list of play options
rps = ["Rock", "Paper", "Scissors"]





# main function
def myGame():
    #assign a random play to the computer
    computer = rps[randint(0,2)]
    #set player to False
    player = False
    while player == False:
    #set player to True
        player = input("Select: Rock, Paper, Scissors?").capitalize()
        if player == computer:
            print(f"Computer selects {computer}, you selected {player}\nIt's a tie") 

        elif player == "Rock":
            if computer == "Paper":
                print(f"Computer selects {computer}, you selected {player}\nThe computer wins!")
            else:
                print(f"Computer selects {computer}, you selected {player}\nYou win!")

        elif player == "Paper":
            if computer == "Scissors":
                print(f"Computer selects {computer}, you selected {player}\nThe computer wins!")
            else:
                print(f"Computer selects {computer}, you selected {player}\nYou win!")
                
        elif player == "Scissors":
            if computer == "Rock":
                print(f"Computer selects {computer}, you selected {player}\nThe computer wins!")
            else:
                print(f"Computer selects {computer}, you selected {player}\nThe computer wins!")
                
        else:
            print("That's not a valid play. Check your spelling!")

        
        #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = rps[randint(0,2)]


myGame()