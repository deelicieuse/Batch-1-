print("Prog02: This program asks for 2 numbers and checks if they're equal.")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input.")
    exit()

if num1 != num2:
    print("Not Equal")
else:
    print("Both numbers are equal.")
