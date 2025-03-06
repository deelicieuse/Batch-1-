print("Prog09: This program prints all numbers from 0 to 100 except those ending in 0 or 5.")
for num in range(101):
    if num % 10 not in (0, 5):
        print(num, end=" ")
print()
