# removeprefix() remove the characters at the beginning of the string that matches the function parameter.
# Create a program that do the same functionality without using removeprefix() function.

# Input of text and removing prefix
text = input("Enter any text: ")
remove_prefix = input("Enter prefix to remove (must include the first character of your text): ")

# Removes characters at the beginning of the string
if text[:len(remove_prefix)] == remove_prefix:
    print(text[len(remove_prefix):])
else:
    print(text)