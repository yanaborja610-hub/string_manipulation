# Create a program that ask user to input 2 numbers.Print the result when the first number is raised to the second number.

# Input of numbers
first_number = float(input("Enter a number: "))
second_number = float(input("Enter another number: "))

# Logic of the program and displaying the result
result = first_number ** second_number
print(f"{first_number} raised to {second_number} = {result}")