# Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# Input of 10 numbers
numbers = []
for i in range(10):
    numbers.append(float(input("Enter a number: ")))

# Logic and displaying of the result
for number in set(numbers): # Using set to make duplicates appear only once
    if numbers.count(number) > 1: # Will count whether number is greater than 1
        print(number) # Displaying all number that have duplicate