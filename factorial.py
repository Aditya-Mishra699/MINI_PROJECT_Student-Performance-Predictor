#Factorial of a number
n = int(input("enter ur fav number : "))
product = 1
for i in range (1,n+1):  
    product = product * i
    
print(f"the factorial of ur fav number {n} is {product}")