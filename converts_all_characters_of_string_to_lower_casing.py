# lower() converts all characters of the string into lower case.
# Create a program that do the same functionality without using lower() function.

# For the input of text
text = input("Enter text in capital letters: ")
result = "" # Empty string for later use

# Using for loop in converting capital letters to small case
for characters in text:
    if 'A' <= characters <= 'Z': # Checks if letters are uppercase
        result += chr(ord(characters) + 32) # Converts by adding 32 to its ASCII value
    else:
        result += characters # Keeps small characters unchanged