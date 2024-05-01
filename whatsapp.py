import pywhatkit
from datetime import datetime, timedelta

# Calculate the current time plus a short delay
current_time = datetime.now()

# Extract hour and minute from the send_time
hour = current_time.hour
minute = current_time.minute

# Attempt to send a Whatsapp message

try:
	pywhatkit.sendwhatmsg("+254115251183","Hello there!", hour, minute, wait_time=15)
	print("Successfully sent!")
	
except Exception as e:
	print("An unexpected error!", e)

# send messages with python
# pip install pywhatkit