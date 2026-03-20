# Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# Input of 10 numbers
numbers = []
for i in range(10):
    numbers.append(float(input("Enter a number: ")))

# Displaying all the numbers but numbers with duplicate appear only once
print(set(numbers))