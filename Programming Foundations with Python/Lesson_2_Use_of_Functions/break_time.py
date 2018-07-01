import datetime
import time
import webbrowser

total_breaks = 3 # number of loops
break_count = 0 # counter for the while loop

print("This program started on " + str(datetime.datetime.now()))
while break_count < total_breaks:
    time.sleep(2 * 60 * 60) # converts 2 hours to seconds
    webbrowser.open("https://www.youtube.com/watch?v=rXV_AicZRTU")
    break_count += 1