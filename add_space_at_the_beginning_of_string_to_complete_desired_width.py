# rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter.
# Create a program that do the same functionality without using rjust() function.

# For the input of text and desired width
text = input("Enter text: ")
width = int(input("Enter total width: "))

# Tells how many spaces to add
spaces_needed = width - len(text)

# Adds the spaces to the string
if spaces_needed > 0:
    result = " " * spaces_needed + text
else:
    result = text

# Displays result
print("'" + result + "'")