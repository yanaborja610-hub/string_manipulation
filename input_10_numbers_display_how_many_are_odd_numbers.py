# Create a program that ask user to input 10 numbers. Print how many are odd numbers.

numbers = [] # list for input
count = 0 # default count of odd numbers

# Input of 10 numbers
for i in range(10):
    num = (float(input("Enter a number: ")))
    (numbers.append(num))