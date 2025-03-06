print("Prog01: This program asks for 2 numbers and prints the smaller one.")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input.")
    exit()

if num1 < num2:
    print("The smaller number is:", num1)
elif num2 < num1:
    print("The smaller number is:", num2)
else:
    print("Both numbers are equal.")
