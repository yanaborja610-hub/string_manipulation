# Create a program that ask user to input 2 numbers. Print the bigger number.

# Input of numbers
first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))

# Logic of displaying the bigger number
if first_number > second_number:
    print(f"The bigger number is the first number: {first_number}")
else:
    print(f"The bigger number is the second number: {second_number}")