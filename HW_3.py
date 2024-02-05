continue_calc = True
while continue_calc:

    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

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

    ask_question = input("Do you want to continue (y, n)?: ")
    if ask_question == "y":
        continue_calc = True
    else:
        continue_calc = False


