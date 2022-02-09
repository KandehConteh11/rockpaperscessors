
print("You are about to play the Rock Paper Scissors Game")
print("Welcome To The Rock Paper Scissor Game")

choice= input("You are the first to go. What's your choice 'ROCK', 'PAPER' OR 'SCISSORS'? Choose One.\n").lower()
if choice == "paper":
    print("you win the first round")
else:
    print("You loss the first rounds ")
choice1 =input("welcome to round two. What's your choice 'ROCK', 'PAPER' OR 'SCISSORS'? Choose One.\n").lower()

if choice1 == "paper":
    print("you win the second round")
else:
    print("You loss the second rounds")
choice2 =input("welcome to round Three. What's your choice 'ROCK', 'PAPER' OR 'SCISSORS'? Choose One.\n").lower()
if choice2 == "scissors":
    print("you win the last round")
else:
    print("You loss the last rounds")
if choice == "paper" and choice1 == "paper" and choice2 == "scissors":
    print("HERE WE GO! YOU WIN THE GAME!")
elif choice == "paper" and choice1 == "paper" or choice2 == "scissors":
    print("you narrowly Win. Try Again")
elif choice == "paper" or choice1 == "paper" or choice2 == "scissors":
    print("you Win One out of Three. You Loss! Try Again")
else:
    print("You loss the Game. Try Again")
