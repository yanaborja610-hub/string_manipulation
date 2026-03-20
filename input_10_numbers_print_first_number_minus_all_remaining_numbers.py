#  Create a program that ask user to input 10 numbers. Print the result of the first number minus all the remaining numbers.

# For input of numbers
result = float(input("Enter number 1: "))

for i in range(2, 11):
    result -= float(input(f"Enter number {i}: "))