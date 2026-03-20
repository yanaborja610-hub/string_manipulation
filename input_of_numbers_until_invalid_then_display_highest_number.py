# Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the highest number

numbers = [] # For storing numbers
# While loop to keep on asking until input is invalid
while True:
    user_input = input("Enter a number: ")

    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        break  # Stops when input is invalid

# Prints the highest number from the stored list
if numbers:
    highest = max(numbers)
    print("The highest number is", highest)
else:
    print("No valid numbers were entered.")