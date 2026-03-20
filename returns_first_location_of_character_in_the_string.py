# index() return the first location of the function parameter in the string.
# Create a program that do the same functionality without using index() function.

# Input string and character to find
text = input("Enter text: ")
target = input("Enter character to find: ")

# Find the first appearance of character
position = -1  # Default if not found
for i, character in enumerate(text):
    if character == target:
        position = i
        break

# Display the index of the inputted character
if position != -1:
    print(f"'{target}' first appears at index {position}.")
else:
    print(f"'{target}' not found in the string.")