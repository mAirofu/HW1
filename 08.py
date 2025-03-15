num1 = int(input("First number:"))
num2 = int(input("Second number:"))
math = input("Math symbol(+, -, *, /):")
if math == "+":
    print("First number + Second number =",num1 + num2)
elif math == "-":
    print("First number - Second number =", num1 - num2)
elif math == "*":
    print("First number * Second number =", num1 * num2)
elif math == "/" and num2 == 0:
    print("Division by zero")
elif math == "/":
    print("First number / Second number =", num1 / num2)
