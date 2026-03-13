# Create a program that ask user to input 10 numbers. Print how many are even numbers.

numbers = [] # list for input
count = 0 # default count of even numbers

# Input of 10 numbers
for i in range(10):
    num = (float(input("Enter a number: ")))
    (numbers.append(num))