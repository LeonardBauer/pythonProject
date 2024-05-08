import random

while True:
    rndNum = random.randint(1, 10)
    print(rndNum)
    i = int(input("Guess the number: "))
    if i == rndNum:
        print("Correct!")
    elif i == 0:
        break
    else:
        print("Wrong!")
