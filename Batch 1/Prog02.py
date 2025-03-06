print("Prog02: This program asks you to input 2 numbers and tells you if they are equal.")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input.")
    exit()

if num1 == num2:
    print("Equal")
else:
    print("The numbers are not equal.")
