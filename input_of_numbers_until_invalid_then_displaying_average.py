# Create a program that ask user to input a number,continue asking until the user input is invalid.
# Display the average.

numbers = [] # List for storing numbers
# While loop to keep on asking for a number until invalid
while True:
    try:
        numbers.append(float(input("Enter a number: ")))
    except ValueError:
        break # Stops the loop when value is invalid

# Formula of average and displaying it
average = sum(numbers) / len(numbers)
print("Average:", average)