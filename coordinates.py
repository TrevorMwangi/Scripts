# pip install geopy
# this code enables for finding co-ordinates of cities around the world

from geopy.geocoders import Nominatim

# Create a Geolocator object
geolocator = Nominatim(user_agent="geoapiExercises")

try:
    # Prompt the user to enter a city name
    place = input("Enter city name: ")
 
    # Attempt to geocode the location
    location = geolocator.geocode(place)

    # Check if location is found
    if location:
        # Print the latitude and longitude
        print("Latitude:", location.latitude)
        print("Longitude:", location.longitude)
    else:
        print("Location not found.")

except Exception as e:
    # Handle any exceptions here
    print("An error occurred:", e)
