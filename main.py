import requests
import os


url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Chennai?unitGroup=metric&key=H34HHM9SNNT85Y7EW92AZXW7T&contentType=json"

response = requests.get(url).json()

location = response["address"]
date = response["days"][0]["datetime"]
desc = response["days"][1]["description"]
description = response["description"]
temp = response["currentConditions"]["temp"]
humidity = response["currentConditions"]["humidity"]
conditions = response["currentConditions"]["conditions"]
sunrise = response["currentConditions"]["sunrise"]
sunset = response["currentConditions"]["sunset"]
os.system('cls')
print("PY Weather\nA quick way to get your weather info!\n")
print(f"{location} | {date}\n")
print(conditions)
print(f"{description}")
print(f"{desc}\n")
print(f"Temperature: {int(temp)}°C")
print(f"Humudity: {humidity}%\n")
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}\n")
