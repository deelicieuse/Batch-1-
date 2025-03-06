print("Prog03: This program calculates the sum of two numbers you input.")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}.")
