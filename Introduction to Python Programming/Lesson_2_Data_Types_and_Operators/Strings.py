# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + " accessed the site " + url + " at " + timestamp + ".")
print(username + " accessed the site " + url + " at " + timestamp + ".")

# TODO: Use string concatenation and the len() function. Find the length of a certain
# movie star's actual full name. Store that length in the name_length variable.
# Don't forget that there are spaces in between the different parts of a name!
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + middle_names + family_name) + 2 # For the whitespaces

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
