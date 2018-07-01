# Exercise 1
# Here we'll take the string print_str and print out its letters, one per line.
# We'll guide you step-by-step in the code below for this one.

# For example, print_str below is Water falls, so this should output:

# W
# a
# t
# e
# r

# f
# a
# l
# l
# s

print_str = "Water falls"

# TODO: initialize a counting variable "i" to 0 - you'll use this to track which character of the string you're on

# TODO: write your while header line, comparing "i" to the length of the string

# TODO: here in the body of the loop, print out the current character from the string

# TODO: increment your counter variable in the body of the loop, so you don't loop forever!

i = 0
while i < len(print_str):
    for char in print_str:
        print(char)
        i += 1

# Exercise 2
# Find the Factorial of a Number, using While Loop.
# Example: If number is 6, your code should compute and print the product of 720.

# Start with a sample number for first test - change this when testing your code more!
number = 6
# We'll always start with our product equal to the number
product = number

# TODO: Write while loop header line - how will you tell it when to stop looping?

# TODO: Each time through the loop, what do we want to do to our number?

# TODO: Each time, what do we want to multiply the current product by?

# TODO: Print out final product (how do we indicate this should happen after loop ends?)

while number > 1:
    number -= 1
    product *= number
print(product)

# Exercise 3
# Write a for loop that calculates the factorial of our number
number = 6
# We'll start with the product equal to the number
product = number

# Write a for loop that calculates the factorial of our number
for num in range(1, number):
    product *= num

# print the factorial of your number
print(product)

# Exercise 4
# Suppose you want to count from some number start_num by another number count_by
# until you hit a final number end_num. Use break_num as the variable that you'll
# change each time through the loop.

# Before the loop, what do you want to set break_num equal to?
# How do you want to change break_num each time through the loop?
# What condition will you use to see when it's time to stop looping?

# After the loop is done, print out break_num, showing the value that indicated it
# was time to stop looping.

start_num = 5  # provide some start number
end_num = 100  # provide some end number that you stop when you hit
count_by = 2  # provide some number to count by

# write a while loop that uses break_num as the ongoing number to
# check against end_num

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

# Exercise 5
# Now in addition, address what would happen if someone gives a start_num that
# is greater than end_num. If this is the case, set result to "Oops! Looks like
# your start value is greater than the end value. Please try again." Otherwise,
# set result to the value of break_num.

start_num = 200  # provide some start number
end_num = 100  # provide some end number that you stop when you hit
count_by = 20  # provide some number to count by

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
if start_num > end_num:
    result = "Oops!  Looks like your start value is greater than the end value.  Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)

# Exercise 6
# Write a while loop that finds the largest square number less than an integer
# limit and stores it in a variable nearest_square. A square number is the product
# of an integer multiplied by itself, for example 36 is a square number because
# it equals 6*6.

# For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

num = 0
while (num + 1) ** 2 < limit:
    num += 1
nearest_square = num ** 2

print(nearest_square)
