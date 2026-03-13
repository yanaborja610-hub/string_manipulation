# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# Input of numbers
first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))

# Printing quotient without showing the decimal point
result = first_number / second_number
print(f"{first_number} divided by {second_number} = {int(result)}")