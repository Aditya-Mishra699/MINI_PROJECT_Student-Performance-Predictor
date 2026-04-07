#To print simple numbers with loops
for i in range(1, 11):
    print(i)
    
#To print even numbers from 1 to 10
for i in range(1, 11):
    if i%2==0:
        print(i)

#To print odd numbers from 1 to 10
for i in range(1, 11):
    if i%2!=0:
        print(i)


 #To print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

#To print the table of 5
for i in range(0, 11):
    print("5 x", i, "=", 5*i)     

#To print the table of any number entered by user
num = int(input("Number bol: "))
for i in range(0, 11):
    print(num, "x", i, "=", num*i)

#to print reverse table of any number entered by user
num = int(input("Number bol: "))
for i in range(10, 0, -1):
    print(f"{num} x {i} = {num*i}")


    