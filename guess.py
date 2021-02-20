import random
number=random.randint(1,5)
chances=0
while chances<5:
    guess=int(input("Guess a number between 1 and 9."))
    if number == guess:
        print("YOU WIN!!!!!!")
        break
    elif guess<number:
        print("Your guess was too low")
    else:
        print("Your guess was too high")

chances=chances+1

if not chances<5:
    print("You lost. The number is", number)