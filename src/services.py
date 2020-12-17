import requests
from utils import reformat_weather

def get_weather(id):
    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?units=metric&id={id}&APPID=b21e83e7e234a5fef2cbaff6ee3221f0').json()
    r = reformat_weather(r)
    # print(r)
    return r