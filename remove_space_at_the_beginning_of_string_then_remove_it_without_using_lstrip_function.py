#  lstrip() remove the space characters at the beginning of the string.
#  Create a program that do the same functionality without using lstrip() function.

# Ask for user's input
text = input("Input several spaces before adding text: ")
i = 0 # Initializes count

while i < len(text) and text[i] == " ": # Ensures character is less than the text and checks if a character is a space
    i += 1 # Skips spaces by moving to the first actual character

# Prints the text starting from 1st character to the end
print(text[i:])