# Generator Expressions
# Here's a cool concept that combines generators and list comprehensions! You can actually create a generator in the
# same way you'd normally write a list comprehension, except with parentheses instead of square brackets. For example:

# this produces a list of squares using a list comprehension. It's a single line for-loop.
sq_list = [x ** 2 for x in range(10)]

print(sq_list)

# this produces the same list of squares using a plain for-loop.
squares = []
for x in range(10):
    squares.append(x * x)

print(sq_list)

# this produces an iterator of squares using a generator expression. It's a single line generator.
sq_iterator = (x ** 2 for x in range(10))

# iterating over it
print("Iterating over the generator expression for the first time:")
for n in sq_iterator:
    print(n)
print("Done!")


# this produces an iterator of squares using a generator function.
def sq_generator(n):
    for i in range(n):
        yield i ** 2


# iterating over it
print("Iterating over the generator function for the first time:")
for n in sq_generator(10):
    print(n)
print("Done!")

# Once a generator expression has been consumed, it can’t be restarted or reused.
# So in some cases there is an advantage to using generator functions or class-based iterators.

print("Iterating over the generator function for the second time:")
for n in sq_generator(10):
    print(n)
print("Done!")

print("Iterating over the generator function for the second time:")
for n in sq_iterator:
    print(n)
print("Done!")
