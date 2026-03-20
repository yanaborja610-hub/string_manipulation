# Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display "Unique" after input when the inputted number don't have duplicate.
# Display "Duplicate" after input when the inputted number have duplicate.

numbers = [] # Storing numbers inputted
# While loop to keep on asking for input until invalid
while True:
    try:
        num = float(input("Enter number: "))