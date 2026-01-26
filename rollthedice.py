import random

playing = True
while playing:
    roll = input("roll the dice?: (y/n)").lower
    if roll == "y":
        result1 = random.randint(1,6)
        print (result1)
        again = input("roll again?(y/n): ")
    elif roll == "n":
        print ("sure")
        break
    else :
        print("invalid, try again")
    