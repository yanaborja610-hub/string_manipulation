# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Input of 10 numbers
numbers = []
total = 0
for i in range(10):
    numbers.append(float(input("Enter a number: ")))
    # For adding all the numbers
    total += numbers[i]

# Printing the sum of all numbers
print("The sum of all the numbers are", total)