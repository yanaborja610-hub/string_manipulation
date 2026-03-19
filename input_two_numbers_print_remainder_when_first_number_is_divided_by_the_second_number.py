# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# Input of numbers
first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))

# Printing the remainder without decimal point
if second_number != 0:
    remainder = first_number % second_number
    print("Remainder:", remainder)
else:
    print("Cannot be divided by 0")