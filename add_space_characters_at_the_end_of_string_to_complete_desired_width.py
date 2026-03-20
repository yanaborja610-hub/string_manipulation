# ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter.
# Create a program that do the same functionality without using ljust() function.

# For the input of text and desired width
text = input("Enter text: ")
width = int(input("Enter total width: "))

# Tells how many spaces to add
spaces_needed = width - len(text)

# Adds the spaces to the text
if spaces_needed > 0:
    result = text + " " * spaces_needed
else:
    result = text

# Displays result
print("'" + result + "'")