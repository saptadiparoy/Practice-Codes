#q1
'''
class Calculator:
    def add(self, *args):
        total_sum = sum(args)
        print(f"The sum is: {total_sum}")

calc = Calculator()

calc.add(8,45,7)
'''
#q2 - 
'''
class circle():
    def draw(self):
        print ("Drawing a circle.")
class square():
    def draw(self):
        print ("Drawing a square.")

c1 = circle()
s1 = square()

c1.draw()
s1.draw()
'''

#q3 read a file line by line
'''
f = open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\python\\jury practice\\sample.txt", "r")
for line in f:
    print(f"{line.strip()}")
'''

#q4 - delete word from dictionary
dict1 = {1 : 'x',
         2 : 'y',
         3 : 'z'}
del dict1[2]
print (dict1)
