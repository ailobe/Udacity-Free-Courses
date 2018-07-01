# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.

# page = contents of a web page
page = ('<div id="top_bin"><div id="top_content" class="width960">'
        '<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=')

end_link = page.find(">", start_link)

# It will give us the position of the first " in "url".
# To avoid it being included in url when we slice page,
# e.g. '"http://udacity.com', we'll reassign the value + 1.
start_url = page.find('"', start_link)
start_url += 1

# It will give us the position of the second " in "url",
# but will not be included in the slice.
end_url = page.find('"', start_url)

url = page[start_url:end_url]

print(url)
