print("Prog05: This program calculates the remainder of two numgers.")
try:
    num1 = int(input("Enter the first dividend: "))
    num2 = int(input("Enter the second divisor: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit()

result = num1 % num2
print(f"The remainder when {num1} is divided by {num2} is {result}.")
