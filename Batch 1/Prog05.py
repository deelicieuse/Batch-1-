print("Prog05: This program calculates the quotient (with decimals) of two numbers.")
try:
    num1 = float(input("Enter the dividend: "))
    num2 = float(input("Enter the divisor: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
except ValueError:
    print("Invalid input.")
    exit()

result = num1 / num2
print(f"The quotient of {num1} divided by {num2} is {result}.")
