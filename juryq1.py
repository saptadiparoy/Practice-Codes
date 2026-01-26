#question 1 - make a list and print
"""
list1 = [1 , 2, 3, 4, 5]
print (list1)
"""

#question 2 - age categorisation
"""
def agecheck(age):
    if age >= 0 and age <= 12:
        print ("Youre a child!")
    elif age >= 13 and age < 18:
        print ("Youre a teenager!")
    elif age >= 18 and age <= 50:
        print ("Youre an Adult!")
    else :
        print ("Youre a Senior citizen!")
x = int(input("enter your age:"))
agecheck(x)
"""
#question 3 -file not found error
"""
try :
    f = open("data.txt", "r")
    print (f.read)
except:
    if FileNotFoundError:
        print ("This file does not exist")
"""