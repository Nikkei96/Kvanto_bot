import telebot
from telebot import types
#local imports
import config
import text
import data


bot = telebot.TeleBot(config.TOKEN, parse_mode="Markdown")

def kbd_main():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in data.main_btns:
        keyboard.add(btn)
    return keyboard

def kbd_kvantums():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for key, value in data.kvant_btns.items():
        keyboard.add(types.InlineKeyboardButton(value, callback_data=key))
    return keyboard


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, text.about_bot, reply_markup=kbd_main())

@bot.message_handler(content_types=["text"])
def answer_menu_items(message):
    try:
        if message.text == data.main_btns[0]:
            bot.send_photo(message.chat.id, open(data.images["kv_logo"], "rb"))
            bot.send_message(message.chat.id, text.about_kvantorium)
        elif message.text == data.main_btns[1]:
            bot.send_photo(message.chat.id, open(data.images["kv_tsk_logo"], "rb"), reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, text.about_kvantorium_tsk, reply_markup=kbd_kvantums())
    except:
        bot.send_message(message.chat.id, text.error)

@bot.callback_query_handler(func=lambda call: True)
def answer_callback(call):
    if call.data != "menu":
        bot.send_photo(call.message.chat.id, open(data.images[f'{call.data}_logo'], "rb"))
        bot.send_message(call.message.chat.id, text.kvantums[call.data], reply_markup=kbd_kvantums())
    else:
        bot.send_message(call.message.chat.id, "Выберите элемент меню 👇", reply_markup=kbd_main())


bot.polling()