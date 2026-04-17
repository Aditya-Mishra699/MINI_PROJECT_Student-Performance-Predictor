# handling divide by zero error

try:
    a = int(input("Enter number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")