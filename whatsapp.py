import pywhatkit
from datetime import datetime, timedelta

# Calculate the current time plus a short delay
current_time = datetime.now()
send_time = current_time + timedelta(seconds=20)

# Extract hour and minute from the send_time
hour = send_time.hour
minute = send_time.minute

# Attempt to send a Whatsapp message

try:
	pywhatkit.sendwhatmsg("+254115251183","Hello there!", hour, minute)
	print("Successfully sent!")
	
except Exception as e:
	print("An unexpected error!", e)

# send messages with python
# pip install pywhatkit