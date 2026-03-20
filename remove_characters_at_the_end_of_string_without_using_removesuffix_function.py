# removesuffix() remove the characters at the end of the string that matches the function parameter.
# Create a program that do the same functionality without using removesuffix() function.

# For the input of text and suffix to be removed
text = input("Enter text: ")
suffix = input("Enter suffix to remove: ")

# Remove characters at the end of the string
print(text[:-len(suffix)] if text.endswith(suffix) and suffix else text)