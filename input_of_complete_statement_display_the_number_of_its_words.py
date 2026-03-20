# Create a program that ask the user to input a complete statement.
# Print the number of words in the input.

# For the input of name
name = input("Input a complete statement: ")

# Displaying the number of words
number_of_words = len(name.split())
print("Number of words: ", number_of_words)