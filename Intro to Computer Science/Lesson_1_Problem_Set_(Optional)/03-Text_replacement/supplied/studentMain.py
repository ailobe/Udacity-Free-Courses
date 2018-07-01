###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1
marker1 = "AFK"
replacement1 = "away from keyboard"
line1 = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
marker2 = "EY"
replacement2 = "Eyjafjallajokull"
line2 = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."


###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###


def replace_marker(line, marker, replacement):
    start_marker = line.find(marker)
    end_marker = line.find(marker) + len(marker)
    replaced = line[:start_marker] + replacement + line[end_marker:]
    return replaced


print(replace_marker(line1, marker1, replacement1))
print(replace_marker(line2, marker2, replacement2))
# Example 1 output should be:
# >>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
# >>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.
