# Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Input of 10 numbers
numbers = []
for i in range(10):
    numbers.append(float(input("Enter a number: ")))

# Displaying all numbers that doesn't have any duplicate
for number in numbers:
    if numbers.count(number) == 1:
        print(number)