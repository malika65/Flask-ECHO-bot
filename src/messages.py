import telebot, time
from services import get_weather

def hello_message(user_name):
    return f"Привет {user_name}\n Я бот , который скажет погоду в Бишкеке на сегодня"
    
def temp_message(message):
    tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
    s = get_weather(message)
    description = s['description']
    humidity = s['humidity']
    feels_like = s['feels_like']
    temp = s['temp']

    return f"Temperature : {temp}\nFeels like : {feels_like}\nHumidity : {humidity}\nDescription : {description} "
    