from cmath import sqrt


print("Select an option below: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE")
print("6. SQUARE ROOT")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The answer is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The answer is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The answer is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The answer is " + str(int(num1) / int(num2)))
elif operation == "5":
    num = input("Enter number: ")
    print("The answer is " + str(int(num) * int(num1)))
elif operation == "6":
    num = int(input("Enter number: "))
    print("The answe is " + str(int(num)**0.5))
else:
    print("INVALID ENTRY!")



 