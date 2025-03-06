print("Prog04: This program calculates the product of two numbers.")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input.")
    exit()

result = num1 * num2
print(f"The product of {num1} and {num2} is {result}.")
