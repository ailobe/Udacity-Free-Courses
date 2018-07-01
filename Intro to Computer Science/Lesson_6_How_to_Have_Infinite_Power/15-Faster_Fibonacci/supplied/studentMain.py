# Define a faster fibonacci procedure that will enable us to computer
# fibonacci(36).

def fibonacci(n):
    current = 0
    after = 1
    result = 0
    for i in range(0, n):
        current, after = after, current + after
    return current


'''
    last = n - 1
    next_to_last = n - 2
    while result == 0:
        result += last + next_to_last
        last += 1
        next_to_last += 1
    return result
'''

print(fibonacci(36))
# >>> 14930352

print(fibonacci(4))
# >>> 3
