#question 1 - operations on set
'''
set1 = {1,2,3, "apple", "bear"}
print (set[3])
for x in set1 :
    print (x)
print (set1)
print ("apple" in set1)
'''

#question 2 - divisibility by 5 and 11
'''
num = int(input("Enter a number:    "))
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11.")
else:
    print(f"{num} is not divisible by both 5 and 11.")
'''

#question 3 - integer input but if string handle error
'''
try:
    number = int(input("Enter a number:     "))
    print (number)

except :
    if ValueError:
        print ("numer dalo yawr </3")
'''

#question 4 - string and actions on it
'''
x = "some string value"
print (len(x))
print (x[2:7])
print (x)
'''
#question 5 - function to comapre numbers
'''
def compare():
    x = int(input("Enter a number:   "))
    y = int(input("Enter a number:   "))
    if x > y :
        print (f"{x} is greater than {y}")
    elif x < y :
        print (f"{y} is greater than {x}")
    else :
        print(f"both are equal")

compare()
'''

#question 6 - sum of numbers in a file
''''''
f = open('sometext.txt', 'w')
f.write('4567')

f = open('sometext.txt', 'r')
content = f.readlines()

total = 0

for line in content:
    for char in line:
        if char.isdigit():
            total += int(char)

print("The sum of digits is:", total)
