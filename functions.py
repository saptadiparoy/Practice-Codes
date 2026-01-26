def area_of_circle (r): #parameter
    ar_circle = (22/7)*r*r
    print (f"area of circle is: {ar_circle}")
area_of_circle(7)#arguement

def area_of_rectangle (l,b):
    ar_rect = l*b
    print (f"area of rectangle is: {ar_rect}")
area_of_rectangle(3,7)

def area_of_square(s):
    ar_sqr = s*s
    print (f"area of square is: {ar_sqr}")
area_of_square(5)


#when defining no parameter
def greeting():
    print("hello")
greeting()

#using return
def add(a,b):
    return a+b
add(3,4)

def sum_input ():
    a = int(input("a : "))
    b = int(input("b : "))
    sum_inp = a + b
    print ("sum =",sum_inp)
sum_input()
