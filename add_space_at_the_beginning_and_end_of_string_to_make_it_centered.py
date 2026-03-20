# center() add space characters at the beginning and at the end of the string to print the string at the center.
# Create a program that do the same functionality without using center() function.

# For the input of text and desired width
text = input("Enter text: ")
width = int(input("Enter desired width: "))

spaces_needed = width - len(text) # Tells how many spaces to add
left = spaces_needed // 2 # Divides spaces evenly for the left side
right = spaces_needed - left # Remaining spaces goes to the right side