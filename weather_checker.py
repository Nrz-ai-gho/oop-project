# import requests

# url = "https://api.open-meteo.com/v1/forecast"

# params = {
#     "latitude": 42.87,
#     "longitude": 74.59,
#     "current": "temperature_2m,wind_speed_10m",
# }

# try:
#     response = requests.get(url, params=params, timeout=10)
#     response.raise_for_status()
#     data = response.json()
    
#     weather = data["current"]
#     print(f"Temperature{weather["temperature_2m"]} C")
#     print(f"Wind{weather["wind_speed_10m"]} km/m")
# except requests.exceptions.RequestException as e:
#     print("sisba zap:", e)

import requests

try:
    lat = float(input("Введите число :"))
    lon = float(input("Введите число :")) 
except:
    print("Введите число :")
    exit()
    
    
url = "https://api.open-meteo.com/v1/forecast"

params = {
     "latitude": lat,
     "longitude": lon,
     "current": "temperature_2m,wind_speed_10m,relative_humidity_2m,is_day,wind_direction_10m,wind_gusts_10m"
}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    
    weather = data["current"]
    print(f"Температура: {weather["temperature_2m"]} C")
    print(f"Ветер: {weather["wind_speed_10m"]} км/ч")
    print(f"Относительная влажность: {weather["relative_humidity_2m"]}")
    print(f"Направление ветра: {weather["wind_direction_10m"]} км/ч")
    print(f"Порывы ветра: {weather["wind_gusts_10m"]} км/ч")
except requests.exceptions.RequestException as e:
    print("Ошибка:", e)

