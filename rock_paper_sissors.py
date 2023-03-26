import random

exit = False
user_scores = 0
computer_scores = 0

while exit == False:
    option = ["rock", "paper", "scissors"]
    user_input = input("choose rock, paper, scissors :")
    computer_choice = random.choice(option)

    if user_input == "exit":
        print("Game ended...")
        print("You won a total scores of this "+str(user_scores)+" and computer total scores is "+str(computer_scores))
        exit = True

    if user_input == "rock":
        if computer_choice == "rock":
            print("It's a Tie...")
        elif computer_choice == "paper":
            print("Computer wins...")
            computer_scores +=1
        elif computer_choice == "scissors":
            print("You win...")
            user_scores +=1

    elif user_input == "paper":
        if computer_choice == "rock":
            print("You won...")
            user_scores +=1
        elif computer_choice == "paper":
            print("It's a Tie...")
        elif computer_choice == "scissors":
            print("Computer wins...")
            computer_scores +=1
    
    elif user_input == "scissors":
        if computer_choice == "rock":
            print("Computer wins...")
            computer_scores +=1
        elif computer_choice == "paper":
            print("You won...")
            user_scores +=1
        elif computer_choice == "scissors":
            print("It's a Tie...")

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors" :
        print("Invalid input...")
        