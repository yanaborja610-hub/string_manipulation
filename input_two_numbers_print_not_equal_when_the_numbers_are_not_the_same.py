# Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# Input of numbers
first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))

# Logic of displaying not equal when the numbers are not the same
if first_number != second_number:
    print("The numbers are NOT EQUAL")
# When equal
else:
    print("The numbers are EQUAL")