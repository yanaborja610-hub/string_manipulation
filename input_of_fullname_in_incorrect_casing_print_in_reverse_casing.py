# Create a program that ask the user to input their fullname in incorrect casing.
# Print each character of the input in reverse casing.

# For the input of name
name = input("Input your full name in incorrect casing: ")

# Displaying output in reverse casing
name_in_reverse_casing = name.swapcase()
print("Output in reverse casing:", name_in_reverse_casing)