print("Prog06: This program subtracts the next 9 numbers from the first of 10 numbers you provide.")
numbers = []
for i in range(10):
    try:
        number = float(input(f"Enter number {i+1}: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()
    numbers.append(number)

result = numbers[0]
for num in numbers[1:]:
    result -= num
print(f"After subtracting the other 9 numbers from {numbers[0]}, the result is {result}.")
