print("Prog08: This program counts how many of the 10 numbers you input are odd.")
odd_count = 0
for i in range(10):
    try:
        number = int(input(f"Enter integer number {i+1}: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        exit()
    if number % 2 != 0:
        odd_count += 1
print(f"Out of the 10 numbers, {odd_count} are odd.")
