# title() makes all first letter of each word in the string, capital letter. And all other letter in small case.
# Create a program that do the same functionality without using title() function.

# For input of text
text = input("Enter text: ")

# Makes all first letter of each word in the string capital while the rest in small case
print(" ".join(word[:1].upper() + word[1:].lower() for word in text.split()))