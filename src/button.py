from telebot import types
from config import id_osh, id_bishkek
main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

main_markup.add('Погода на сегодня','Эхо бот')


city_choice = types.InlineKeyboardMarkup(row_width=2)
item3 = types.InlineKeyboardButton("Osh", callback_data=id_osh)
item4 = types.InlineKeyboardButton("Bishkek", callback_data=id_bishkek)
city_choice.add(item3, item4)