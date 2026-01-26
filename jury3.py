#question 2 : to check if a word is a palindrome
'''
def palindrome(x):      #defining the function
    reverse  = x[::-1]  #reversing the word
    #checking if reversed word and main word match
    if reverse == x :
        print (f"given word is a palindrome - \n{x} ------- {reverse}")
    else :
        print (f"entered word is not a palindrome - \n{x} ------- {reverse}")

y = input("Enter a word to check:   ")
palindrome(y)
'''

#question 3 - input for two nums, check zero division error
"""

try :
    a = int(input("enter a number:  "))
    b = int(input("enter a number:  "))
    div = a/b
    print (div)
except:
    if ZeroDivisionError:
        print("cant divide with 0")
"""