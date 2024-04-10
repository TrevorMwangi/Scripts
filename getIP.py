import os
import urllib.request as urllib2
import json

# While loop to continuously prompt the user for the target IP
while True:
    ip = input("What is your target IP:  ")
    url = f"http://ipinfo.io/{ip}/json"

    try:
        # Send a request to the API to retrieve the geolocation info
        response = urllib2.urlopen(url + ip)

        data = response.read()
        values = json.loads(data)

        print("IP: " + values["ip"])
        print("City: " + values.get("city", "N/A"))
        print("Region: " + values.get("region", "N/A"))
        print("Country: " + values.get("country", "N/A"))
        print("Location: " + values.get("loc", "N/A"))
        print("ISP: " + values.get("org", "N/A"))

    except Exception as e:
        print("An error occurred:", e)

    choice = input("Do you want to check another IP? (yes/no):  ")
    if choice.lower() != "yes":

        break