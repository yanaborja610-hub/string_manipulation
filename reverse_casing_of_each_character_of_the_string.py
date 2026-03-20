# swapcase() reverse the casing of each of the character of the string.
# Create a program that do the same functionality without using swapcase() function.

# For the input of text
text = input("Enter text in random casing: ")

# Reverses casing of each character on the string
print("".join(character.upper() if character.islower() \
              else character.lower() if character.isupper() \
                    else character for character in text))