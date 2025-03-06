print("Prog04: This program calculates the integer quotient (without decimals) of two numbers.")
try:
    num1 = int(input("Enter the first integer (dividend): "))
    num2 = int(input("Enter the second integer (divisor): "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit()

result = num1 // num2
print(f"The integer quotient of {num1} divided by {num2} is {result}.")
