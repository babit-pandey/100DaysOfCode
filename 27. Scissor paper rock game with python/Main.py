import random

total_input_left=10
no_of_computer_win=0
no_of_human_win=0


print("\t \t \t  r  =  Rock  :   p  =  Paper  :  s =  Scissor (....Enter Q to stop)  \n")

while (total_input_left>0):
    print(f"\n[ Your chance left {total_input_left} ]")
    total_input_left-=1
    human_input = input("Enter Your Choice.......  \n")
    human_input=human_input.lower()
    computer_input = (random.choice(["s","p","k"]))

    if human_input=="q":
        print(".........GAME END.........")
        break

    elif human_input == computer_input:
        print("Both are same !!!!!")

    elif human_input == 'r' and computer_input == 'p':
        print("Computer won.....You lose....!!")
        no_of_computer_win+=1

    elif human_input == 'p' and computer_input == 'r':
        print("You Won !!")
        no_of_human_win+=1

    elif human_input == 'r' and computer_input == 's':
        print("You Won !!")
        no_of_human_win+=1

    elif human_input == 's' and computer_input == 'r':
        print("Computer won.....You lose....!!")
        no_of_computer_win+=1

    elif human_input == 's' and computer_input == 'p':
        print("You Won !!")
        no_of_human_win+=1

    elif human_input == 'p' and computer_input == 's':
        print("Computer won.....You lose....!!")
        no_of_computer_win+=1

    else:
        print("You Entered Wrong input....try again")


print(f"\nComputer score {no_of_computer_win}\n Your score {no_of_human_win}")
