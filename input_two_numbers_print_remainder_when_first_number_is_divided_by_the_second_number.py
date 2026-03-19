# Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
# Input of numbers
first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))

# Printing the remainder
if second_number != 0:
    remainder = first_number % second_number
    print("Remainder:", remainder)
else:
    print("Cannot be divided by 0")