print("Prog01: This program asks you to input 2 numbers and then prints the bigger one.")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

if num1 > num2:
    print("The bigger number is:", num1)
elif num2 > num1:
    print("The bigger number is:", num2)
else:
    print("Both numbers are equal.")
