# rindex() return the first location of the function parameter in the string starting from the last character.
# Create a program that do the same functionality without using rindex() function.

# Input string and character to find
text = input("Enter text: ")
target = input("Enter character to find: ")

# Find last occurrence of the selected character
position = -1
for i in range(len(text)-1, -1, -1):  # Loop from end to start
    if text[i] == target:
        position = i
        break