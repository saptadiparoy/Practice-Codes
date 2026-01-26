#q1 - list and access elements till the last three elements
'''
list1 = [1,2,3,4,5,6,7,8,9]
print (list1[0:-3])
'''
#q3 - class book with display method
'''
class book():
    def  __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print (f"Title: {self.title}")
        print (f"Author: {self.author}")
        print (f"Price : {self.price}")
        print ("--"*10)

b1 = book("Charlie and the chocolate factory", "Roald Dahl", "350")
b2 = book("Metamorphosis", "Franz Kafka", "200")
b3 = book("Norwegian Wood", "Haruki Murakami", "400")

b1.display()
b2.display()
b3.display()
'''
#q3 - valueerror
"""
try :
    a = int(input("Enter a number:"))
    print ("Number is", a)
except:
    if ValueError:
        print("please enter a number")
"""

#q4 - guitar and piano with play method
"""
class guitar():
    def play(self):
        print("Playing guitar")
class piano():
    def play(self):
        print("Playing a piano")

g1 = guitar()
p1 = piano()

g1.play()
p1.play()
"""

#q5 - add a int and string and handle error
'''
try:
    sum = a + 5
    print (sum)
except :
    if TypeError:
        print("cant add number and string")
'''
#q6 - function to detect larger number
'''
def compare(a,b):
    if a > b:
        return f"{a} is greater than {b}"
    if b > a :
        return f"{b} is greater than {a}"
    else:
        return "uhhhh"
print(compare (9,6))
'''
#q7 - union intersection and ddifference
'''
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union1 = A.union(B)
print("using union():",union1)

intersection1 = A.intersection(B)
print ("using intersection():", intersection1)

diff = A.difference(B)
print ("difference (): ", diff)
'''
#q8 - check is a number is positive or negative or zero
'''
def check(a):
    if a > 0 :
        print ("the number is positive")
    if a < 0 :
        print ("the number is negative")
    if a == 0:
        print ("number is equal to 0")

num = int(input("Enter a number to check:   "))
check(num)
'''

#q9 - ask for positve integer
"""
def get_positive_number():
        try:
            a = input("enter a positive number: ")
            num = float(a)
            if num > 0 :
                print ("number is : ", num)
            else :
                print ("please enter a positive number!")
        except :
            if ValueError:
                print ("enter a number!")

get_positive_number()
"""

#q10 - print list and leave out first three elements
"""
list1 = [1,2,3,4,5,6,7,8,9]
print (list1[2:])
"""
#q11 - class animal with method sound and subclasses dog and cat with their sounds
class animal:
    def sound(self):
        print ("specific animal sound.")

class dog(animal):
    def sound(self):
        print ("bark")

class cat(animal):
    def sound(self):
        print ("meow")

c1 = cat()
d1 = dog()
an1 = animal()

c1.sound()
d1.sound()
an1.sound()