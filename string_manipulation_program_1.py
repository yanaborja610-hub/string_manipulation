# Program 1: remove the space characters at the end of the string

# For entering texts
text_input = input("Enter any word: ")

# Verifying length of text before
print("Length Before:", len(text_input))

# Checks and removes the last character until there are no spaces remaining
while text_input[-1] == " ":
    text_input = text_input[:-1]

# Verifying length of the text after
print("Length After:", len(text_input))

# Displaying the word with no space characters at the end of the string
print(text_input)


