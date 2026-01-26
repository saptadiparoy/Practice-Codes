"""
class car:
    def __init__ (self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"brand : {self.brand}")
        print(f"model : {self.model}")
        print(f"price : {self.price}")
        print ("--"*10)

car1 = car("xyz", "abc", 12)

print("car details:")
car1.display_details()

class circle ():
    def __init__(self, r):
        self.r = r
    def area_circum(self):
        area = self.r * self.r * 3.14
        circum = self.r * 2 * 3.14
        print (f"area is = {area}")
        print (f"Circumference of circle is = {circum}")

c1 = circle(7)
c1.area_circum()
"""

try:
    f = open ("sample.txt" , "r")
except :
     if FileNotFoundError :
        print ("it doesnt exist")