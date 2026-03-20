# Create a program that ask the user to input their fullname in incorrect casing.
# Print the input in snake case.

# For the input of name
name = input("Enter your full name in incorrect casing: ")

# For the output in pascal casing
snake_case = "_".join(name.lower().split())
print("Output in snake casing:", snake_case)