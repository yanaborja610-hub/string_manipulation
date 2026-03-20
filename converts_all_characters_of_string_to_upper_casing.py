# upper() converts all characters of the string into upper case.
# Create a program that do the same functionality without using upper() function.

# For the input of text
text = input("Enter text in lower case: ")
result = "" # Empty string for later use

# Using for loop in converting small letters to capital letters
for characters in text:
    if 'a' <= characters <= 'z': # Checks if letters are lowercase
        result += chr(ord(characters) - 32) # Converts by subtracting 32 to its ASCII value
    else:
        result += characters # Keeps small characters unchanged

# Printing result
print(result)