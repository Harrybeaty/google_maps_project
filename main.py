# Interacting with Google Maps API to find driving time and distance between cities.
# User will input start and end destinations.

# pip install googlemaps
import googlemaps

# Read API key from external file, without disclosing in script, more secure.
API = open("google_maps_api.txt", "r")
APIKey = API.read()

# Pass through API key/ client ID
maps = googlemaps.Client(key = APIKey)

# User inpiuts for start and end drive destination
start_destination = input("Where will you begin your drive?\n")
end_destination = input("Where will you end your drive?\n")

# Calculate distance through API
distance = maps.directions(start_destination, end_destination)

# Format API output, because if we just print it we get loads of unnecessary info.
km_distance = (distance[0]['legs'][0]['distance']['text'])
hrs_mins_duration = (distance[0]['legs'][0]['duration']['text'])

print(km_distance)
print(hrs_mins_duration)