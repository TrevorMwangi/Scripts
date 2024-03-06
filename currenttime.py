import time

localtime = time.localtime()
formatted_time = time.strftime("%A, %B %d %Y %H:%M", localtime)
str = "It's now: " + formatted_time

print(str)