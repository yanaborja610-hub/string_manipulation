# Create a program that ask the user to input their fullname with several space characters at the beginning.
# Print the input without the spaces in the beginning.

# For the input of name
name = input("Input your full name with several spaces: ")

# For output
name_without_spaces = name.lstrip()
print("Output without spaces:", name_without_spaces)