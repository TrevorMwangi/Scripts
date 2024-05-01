import pywhatkit


try:
	pywhatkit.sendwhatmsg("+254115251183","Hello there!",23, 11)
	print("Successfully sent!")
	
except:
	print("An unexpected error!")

# send messages with python
# pip install pywhatkit