import pywhatkit

try:
	pywhatkit.sendwhatmsg("+254115251183","Hello there!",21, 23)
	print("Successfully sent!")
	
except:
	print("An unexpected error!")