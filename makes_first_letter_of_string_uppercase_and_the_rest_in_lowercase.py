# capitalize() makes the first letter of the string, capital letter. And all other letter in small case.
# Create a program that do the same functionality without using capitalize() function.

# For the input of text
text = input("Enter text: ")

# Making first letter of string upper case and the rest in lower case
print(text[:1].upper() + text[1:].lower())