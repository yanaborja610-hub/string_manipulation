# isupper() check if all characters of the string is on upper case.
# Create a program that do the same functionality without using isupper() function.

# For the input of text
print("Checks if text is all in upper casing")
text = input("Enter text: ")
text_is_upper = True  # Checks if text is all in upper case

# Also checks for lower case characters
for characters in text:
    if 'a' <= characters <= 'z': # Checks if characters are lower case
        text_is_upper = False # Verifies the statement
        break

# Displaying the result
if text_is_upper:
    print("The text is all IN UPPER CASING")
else:
    print("The text is NOT IN FULL UPPER CASING")