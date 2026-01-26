outcomes = int(input("How many outcomes?"))
winning = int(input("number of outcomes where you win?"))
losing = outcomes - winning
output = input ("view chances of winning or losing? : (win/loss)")

if output == "win" : 
    pwin = (winning/outcomes) *100
    print ("Chances of winning:", pwin)

if output == "loss" : 
    ploss = (losing/outcomes)*100
    print  ("Chances of losing :", ploss)