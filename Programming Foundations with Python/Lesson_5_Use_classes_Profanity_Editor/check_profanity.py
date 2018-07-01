from urllib.request import urlopen
from urllib.parse import quote


def read_text():
    # the path of the text file
    path = r"C:\Users\miriam\PycharmProjects\Udacity\Programming Foundations with Python\Lesson_5_Use_classes_Profanity_Editor\movie_quotes.txt"
    with open(path, 'r') as quotes:
        content = quotes.read()
        print(content, "\n") # If you don't want to print the document, comment this line.
        check_profanity(content)


def check_profanity(text):
    # the with statement automatically closes the file
    # urllib.parse.quote(string) makes string safe for use as URL components
    # by quoting special characters and appropriately encoding non-ASCII text
    with urlopen("http://www.wdylike.appspot.com/?q=" + quote(text)) as wdyl:
        output = str(wdyl.read())  # convert bytes to str
        if "true" in output:  # finds substring in string
            print("Profanity Alert!!")
        elif "false" in output:
            print("This document has no curse words!")
        else:
            print("Could not scan the document properly.")


read_text()
