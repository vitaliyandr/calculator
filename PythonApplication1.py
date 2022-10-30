print ("Welcome to the best calculator")

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))
action = input('Enter your action(+ - / * ): ')


if action == '+':
    res = number_1 + number_2
    print("Ur result" + " " + str(res))
elif action == '-':
    res = number_1 - number_2
    print("Ur result" + " " + str(res))
elif action == '/':
    if number_2 == 0:
        print("Second number cannot be zero")
    else:
        res = number_1 / number_2
        print("Ur result" + " " + str(res))
elif action == '*':
    res = number_1 * number_2
    print("Ur result" + " " + str(res))
else:
    print("Entered wrong number/sign")
print("Good luck!")