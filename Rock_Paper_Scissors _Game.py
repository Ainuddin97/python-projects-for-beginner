                        # Stone-Paper-Scissor
import random
randomChoice = random.choice(["Stone","Paper","Scissor"])
print("Enter Guess among these: 1. Stone  2. Paper 3. Scissor")
userGuess  = input("Enter your choice:")
if (userGuess == randomChoice):
    print("Tie")
elif ((userGuess == "Scissor") and (randomChoice == "Paper")):
    print("You Won")
elif ((userGuess == "Stone") and (randomChoice == "Paper")):
    print("You Won")
elif ((userGuess == "Stone") and (randomChoice == "Scissor")):
    print("You Won")
else:
    print("You Loose")
print("Computers Choice was ", randomChoice)