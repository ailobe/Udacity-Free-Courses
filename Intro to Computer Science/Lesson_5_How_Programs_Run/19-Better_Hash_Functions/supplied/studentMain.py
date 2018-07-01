# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

# https://discussions.udacity.com/t/challenging-the-professor-testing-times-need-your-help-to-analyze-this-fun-discovery/121419

def hash_string(keyword, buckets):
    hash = 0
    for char in keyword:
        hash += ord(char)
    return hash % buckets


print(hash_string('a', 12))
# >>> 1

print(hash_string('b', 12))
# >>> 2

print(hash_string('a', 13))
# >>> 6

print(hash_string('au', 12))
# >>> 10

print(hash_string('udacity', 12))
# >>> 11
