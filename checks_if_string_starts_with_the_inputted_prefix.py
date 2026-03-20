# startswith() check if the string beginning part matches the function parameter.
# Create a program that do the same functionality without using startswith() function.

# For input of text and prefix
print("Checks if the text starts with the inputted prefix")
text = input("Enter text: ")
prefix = input("Enter prefix: ")

# Checking whether the inputted prefix matches with the beginning of the string
print(text[:len(prefix)] == prefix)