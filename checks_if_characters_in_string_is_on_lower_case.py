# islower() check if all characters of the string is on lower case.
# Create a program that do the same functionality without using islower() function.

# For the input of text
print("Checks if text is all in lower casing")
text = input("Enter text: ")
text_is_lower = True  # Checks if text is all in lower case

# Also checks for upper case characters
for characters in text:
    if 'A' <= characters <= 'Z': # Checks if characters are upper case
        text_is_lower = False # Verifies the statement
        break