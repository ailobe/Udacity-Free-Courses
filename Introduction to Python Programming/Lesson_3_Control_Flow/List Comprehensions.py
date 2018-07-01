# Quiz: Extract First Names
# Use a list comprehension to create a new list first_names containing just the
# first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name[:name.find(" ")].lower() for name in names]
# first_names = [name.split()[0].lower() for name in names]
print(first_names)

# Quiz: Multiples of Three
# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

multiples_3 = [n * 3 for n in range(1, 21)]
print(multiples_3)

# Quiz: Filter Names by Scores
# Use a list comprehension to create a list of names passed that only include those that scored at least 65.

scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

passed = [name for name in scores if scores[name] >= 65]
# passed = [name for name, score in scores.items() if score >= 65]
print(passed)
