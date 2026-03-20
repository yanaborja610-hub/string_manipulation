# count() return how many time the function parameter appear in the string.
# Create a program that do the same functionality without using count() function.

# Input string and character to count
text = input("Enter text: ")
characters = input("Enter character to count: ")

# Count number of character appearance
count = 0
for character in text:
    if character == characters:
        count += 1

# Display result
print(f"The character '{characters}' appears {count} times.")