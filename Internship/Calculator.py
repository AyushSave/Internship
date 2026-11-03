print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Answer:", num1 + num2)

elif operation == "-":
    print("Answer:", num1 - num2)

elif operation == "*":
    print("Answer:", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Answer:", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operation")
