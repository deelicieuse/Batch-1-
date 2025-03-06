print("Prog06: This program raises the first number to the power of the second number.")
try:
    num1 = float(input("Enter the base number: "))
    num2 = float(input("Enter the exponent: "))
except ValueError:
    print("Invalid input.")
    exit()

result = num1 ** num2
print(f"{num1} raised to the power of {num2} is {result}.")
