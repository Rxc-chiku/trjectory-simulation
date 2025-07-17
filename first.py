import random
a = random.randint(1,8)
while True:
    userChoice = int(input('Guess the target:'))
    if (userChoice == a):
        print("success : Correct Guess!!")
        break
    elif(userChoice < a):
        print("no no your number is small")
    else:
        print("no no your number is big")

print("_______GAME OVER_______")
6