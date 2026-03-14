# Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# Input of number
print("Input any number between 0-1000")
number = (int(input("Enter a number: ")))

# Printing the number in 6 digit format
print("Output:", f"{number:06d}")