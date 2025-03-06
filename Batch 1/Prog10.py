print("Prog10: This program prints all numbers from 0 to 100 except those that end with 0.")
for num in range(101):
    if num % 10 != 0:
        print(num, end=" ")
print()
