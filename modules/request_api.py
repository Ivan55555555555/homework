import requests
#Ця строка імпортує requests.
from .read_json import read_json
#Ця строка імпортує функцію read_json.
import json
#Ця строка імпортує json.
data_api = read_json(name_file= 'config_api.json')
#Ця строка створює перемінну data_api, яка застосовує функцію read_json.
API_KEY = data_api['api_key']
#Ця строка отримує наш ключ api.
CITY_NAME = data_api['city_name']
#Ця строка отримує наше місто.
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#Ця строка показує переміннам API_KEY та CITY_NAME де брати інформацію про погоду у нашому місті.
response = requests.get(URL)
#Ця строка отримує інформацію про погоду у нашому місті.
if response.status_code == 200:
    #Ця строка перевіряє отримали ми інформацію про погоду у нашому місті, чи ні.
    data_dict = json.loads(response.content)
    #Ця строка переводе байти отриманної інформації про погоду у нашому місті у str.
    print(json.dumps(data_dict, indent= 4))
    #Ця строка перетворює str отриманної інформації погоду у нашому місті в словарь.