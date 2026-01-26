#take input for table
num = int(input("enter number for table: "))

#get table for user's input using for loop
for i in range (1 ,11):
    i = num*i
    print (i)

#for user entered start and end of table
start =  int(input("start of table:"))
end =  int(input("end of table: "))

for f in range (start , end+1 ):
    f = num*f
    print (f)
