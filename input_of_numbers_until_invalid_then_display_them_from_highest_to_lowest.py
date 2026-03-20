# Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number from highest to lowest. Clue: sort() function

numbers = [] # For storing numbers
# While loop to keep on asking until input is invalid
while True:
    user_input = input("Enter a number: ")

    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        break  # Stops when input is invalid

# Printing them from highest to lowest
numbers.sort(reverse=True) 
print(numbers)