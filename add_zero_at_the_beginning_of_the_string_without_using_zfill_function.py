# zfill() add zero characters at the beginning of the string to
# complete the number of characters specifies in function parameter.
# Create a program that do the same functionality without using zfill() function.

# For the input of text and desired width
text = input("Enter text: ")
width = int(input("Enter total width: "))

# Add zeros at the beginning to reach the desired width
result = "0" * max(width - len(text), 0) + text

# Display result
print("'" + result + "'")