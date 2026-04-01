#q1 - class circle and calculate area
'''
class circle():
    def __init__(self, r):
        self.r = r
    def area(self):
        area = self.r * self.r * 3.14
        print (f"area of circle is: {area}")

c1 = circle(7)
c1.area()
'''

#q2 - list and slice it
'''
list1 = [1,2,3,4,5,6,7,8,9]
print (list1[3:7])
'''

#q3 - factorial of a number
#import factorial
'''
def fact(x):
    if x == 0 :
        return 1
    return x * fact(x-1)
    
num = int(input("enter a number:    "))
print(fact(num))
'''

#q3 - take input for two numbers and divide and handle zerodiv and value error
def division():

    try:
        a = int(input("enter a number:     "))
        b = int(input("enter a number:     "))
        div = a/b
        print(f"Answer is: {div}")
    
    except ZeroDivisionError:
        print ("cant divide by zero")
    except ValueError:
        print ("Enter a number please")

division() 
