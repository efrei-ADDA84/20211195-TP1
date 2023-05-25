import requests
import json 

lat = 48.866667
lon = 2.333333
api_key = "5a0814f7a4cf0f902c7eb4edd74f0c4f"

complete_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"


response = requests.get(complete_url)

if response.status_code == 200:
    
    data = response.json()
    
    temp_kel = data["main"]["temp"]
    temp_cel = temp_kel - 273.15
    
    weather_description = data["weather"][0]["description"]
    
    print(f"The temperature is {temp_cel}°C")
    print(f"The weather is {weather_description}")
    
else:
    print("Erreur lors de la récupération des données météorologiques")