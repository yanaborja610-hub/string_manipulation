# Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number with the most number of duplicate.

numbers = [] # For storing numbers
# Using while loop to keep input going until input is invalid
while True:
    try:
        numbers.append(float(input("Enter a number: ")))
    except ValueError:
        break # Stops the loop