# Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# Input of numbers
first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))

# Displaying all the numbers between the 2 numbers in ascending or descending order
if first_number < second_number:
    i = first_number + 1
    while i < second_number:
        print(i)
        i += 1
else:
    i = first_number - 1
    while i > second_number:
        print(i)
        i -= 1