#q1 - check is two lists are equal
'''
l1 = [1,2,3,4,5]
l2 = [1,2,3,4]
print (l1 == l2)
l2 = [1,2,3,4,5]
print (l1 == l2)
'''

#q2 - class car with display method
'''
class car():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print (f"Car brand: {self.brand}")
        print (f"Model : {self.model}")
        print (f"Price : {self.price}")
        print("--"*10)

c1 = car("xyz", "abc", "12")
c2 = car("abc", "xyz", "45")
c1.display()
c2.display()
'''
#q3 - square root
'''
import math
print (int(math.sqrt(81)))
'''

#grading funtion
'''
def grading(x):
    if x >= 90 :
        print ("Your grade is :A")
    elif x >= 80 and x < 90:
        print ("Your grade is :B")
    elif x >= 70 and x < 80:
        print ("Your grade is :C")
    elif x >= 50 and x < 70:
        print ("Your grade is :D")
    elif x >= 40 and x < 50:
        print ("Your grade is :E")
    elif x < 40 :
        print ("Your grade is :F")
    else : 
        print ("enter valid grade")
def percentage():
    sub1 = float(input("Enter score of subject 1:  "))
    sub2 = float(input("Enter score of subject 2:  "))
    sub3 = float(input("Enter score of subject 3:  "))

    avg  = (sub1+sub2+sub3)/300
    percent = avg*100
    print (f"Your percentage is: {percent}")

    grading(percent)

percentage()
'''
