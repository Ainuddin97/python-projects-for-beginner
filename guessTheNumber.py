                           # Guess the number
import random
randomNumbers = random.randint(1,10)
print(randomNumbers)
userGuess = int(input("Enter you Guess:"))
if (userGuess == randomNumbers):
    print("Congratulations")
elif (((randomNumbers/2 > userGuess)) or ((randomNumbers*2) < userGuess)):
    print("Sorry!! you are too far from the random number")
elif (((randomNumbers/2 < userGuess)) or ((randomNumbers*2) > userGuess)):
    print("You were very close")

else:
    print("You Losse")