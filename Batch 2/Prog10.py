print("Prog10: This program prints all numbers between two numbers you input (excluding the endpoints).")
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit()

if num1 == num2:
    print("The numbers are the same; there are no numbers between them.")
else:
    # Ensure start is the smaller number
    start, end = (num1, num2) if num1 < num2 else (num2, num1)
    if end - start <= 1:
        print("There are no numbers between the given numbers.")
    else:
        print(f"Numbers between {start} and {end} are:")
        for num in range(start + 1, end):
            print(num, end=" ")
        print()
