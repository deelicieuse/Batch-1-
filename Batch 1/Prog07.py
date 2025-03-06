print("Prog07: This program calculates the sum of 10 numbers that you provide.")
total = 0
for i in range(10):
    try:
        number = float(input(f"Enter number {i+1}: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()
    total += number
print(f"The total sum of the numbers is: {total}.")
