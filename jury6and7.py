#q1 - operations ona string
'''
x = str("sOmE stRiNg VaLuE")
print (x.lower())
print (x.upper())
'''

#q2 - module to calculate area of triangle
'''
def area_tri(x,y):
    area = x * y * 0.5
    print (f"area of triangle is : {area}")

b = int (input("enter base:     "))
h = int (input("enter height:   "))
area_tri(b,h)

#import areaoftriangle
'''
#q3 - dictionary and shit
'''
dict1 = {1:"a",
         2:"b",
         3:"c",
         4:"d"}
dict1[5] = "e"
print (len(dict1))
print (dict1[3])
print (dict1)
for key in dict1:
    print (key)
'''
#q4 - factorial of a number
'''
import math
num = int(input("Enter number:  "))
fact = math.factorial(num)
print (f"Factorial of number is: {fact}")
'''
