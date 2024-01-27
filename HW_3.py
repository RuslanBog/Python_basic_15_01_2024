number_1 = float(input("Enter first number:"))
number_2 = float(input("Enter second number:"))
operator = input("Enter an operator (+, -, *, /):")

if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "/":
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("You can't divide by zero")
else:
    print("Try again")

