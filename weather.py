# API CALLS
import requests

# api_address = "http://api.openweathermap.org/data/2.5/weather?appid=4f152fe40915295e05a97c1cdd65151d&q="


lat = 15.912899800000002
long = 79.7399875

api_address = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=4f152fe40915295e05a97c1cdd65151d"


json_data = requests.get(api_address).json()
print(json_data["weather"][0]["description"])