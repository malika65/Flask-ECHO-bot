import os

import telebot, time
from messages import hello_message
from flask import Flask, request
from button import main_markup

import config
from services import get_weather

server = Flask(__name__)
bot = telebot.TeleBot(config.token)

@server.route("/",methods=["POST"])
def receive_update():
    bot.process_new_updates(
        [telebot.types.Update.de_json(
            request.stream.read().decode("utf-8"))])
    return {"ok": True}



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id,hello_message(message.from_user.username),reply_markup=main_markup)
   
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text == 'Погода на сегодня':
        tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
        s = get_weather()
        description = s['description']
        humidity = s['humidity']
        feels_like = s['feels_like']
        temp = s['temp']
        bot.send_message(message.chat.id,text = f"Temperature in Bishkek for {tconv(message.date)}\nTemperature : {temp}\nFeels like : {feels_like}\nHumidity : {humidity}\nDescription : {description} " )
    else:
        bot.send_message(message.chat.id, message.text)


@server.route('/' + config.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    s = bot.set_webhook(url='https://c71070778b9d.ngrok.io' + config.token)
    if s:
        return print("webhook setup ok")
    else:
        return print("webhook setup failed")


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

# if __name__ == '__main__':
#     bot.polling(none_stop = True)