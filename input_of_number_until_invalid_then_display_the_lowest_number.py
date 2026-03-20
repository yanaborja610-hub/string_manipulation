# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

numbers = [] # For storing numbers
# While loop to keep on asking until input is invalid
while True:
    user_input = input("Enter a number: ")

    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        break  # Stops when input is invalid

# Prints the lowest number from the stored list
if numbers:
    lowest = min(numbers)
    print("The lowest number is", lowest)
else:
    print("No valid numbers were entered.")