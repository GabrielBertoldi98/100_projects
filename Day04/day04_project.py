#Rock, paper scissors

import random

plays = random.randint(0, 2)

randomcomputer = random.randint(0, 2)

play = int(input("What do you choose? 0 - rock, 1 - paper, 2 - scissors "))

#Player choose ROCK
if play == 0 and plays == 0:
    print("Computer choose Rock.")
    print("Draw!")
elif play == 0 and plays == 1:
    print("Computer choose Paper.")
    print("You lose!")
elif play == 0 and plays == 2:
    print("Computer choose Scissors")
    print("You Win!")

#Player choose Paper
if play == 1 and plays == 0:
    print("Computer choose Rock.")
    print("You win!")
elif play == 1 and plays== 1:
    print("Computer choose Paper.")
    print("Draw!")
elif play == 1 and plays == 2:
    print("Computer choose Scissors")
    print("You lose!")    

#Player choose Scissors
if play == 2 and plays == 0:
    print("Computer choose Rock.")
    print("You lose!")
elif play == 2 and plays == 1:
    print("Computer choose Paper.")
    print("You win!")
elif play == 2 and plays == 2:
    print("Computer choose Scissors")
    print("Draw!")    