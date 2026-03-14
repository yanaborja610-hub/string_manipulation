# Makes all first letter of each word in the string, capital letter. And all other letter in small case without using title() function.

# Input of string
print("Type anything in random casing")
text = input("Input: ").lower() # Reads string all in lowercase
output = "" # Empty string for later use

# Makes the first letter of a word capital while the following letters small case
for i in range(len(text)):
    output += text[i].upper() \
    if i == 0 or text[i-1] == " " \
        else text[i]