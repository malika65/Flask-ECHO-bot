import telebot
import config
import os
from flask import Flask, request
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

	bot.send_message(message.chat.id,"Hello "
    + message.from_user.first_name+
    ". I am echo bot. I return you your message")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


@server.route('/' + config.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    s = bot.set_webhook(url='https://0cef492b670c.ngrok.io' + config.token)
    if s:
        return print("webhook setup ok")
    else:
        return print("webhook setup failed")


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

# if __name__ == '__main__':
#     bot.polling(none_stop = True)