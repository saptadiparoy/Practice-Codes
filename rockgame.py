import random as rdm
user = input("Start play (rock, paper, scissors)")

game = ["rock", "paper","scissors"]
bot = rdm.choice(game)
print (bot)

if user == bot:
    print ("tie!")

elif user== "paper" and bot=="rock":
    print ("player wins!")

elif user == "rock" and bot == "scissors" : 
    print ("player wins!")

elif user == "scissors" and bot == "paper":
    print ("player wins!")

elif user== "paper" and bot=="scissors" :
    print ("bot wins!")

elif user== "rock" and bot =="paper":
    print ("bot wins!")

elif user == "scissors" and bot== "paper" :
    print ("bot wins!")

else :
    print ("nuh uh")