chance=0
import random
n  = random.randint(1, 9)
while chance<5:
    guess=int(input("please enter a number from 1 to 9"))
    if n > guess:
        print ("You guessed wrong")
        print("you guessed lower than the random number")
        guess=guess-1
    if n < guess :
        print ("You guessed wrong")
        print ("you guessed higher than the random number")
        guess=guess-1
    if n==guess:
        chance=0
        print ("You have guessed the right number")







    