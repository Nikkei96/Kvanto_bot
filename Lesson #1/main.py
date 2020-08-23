import telebot
from telebot import types

#local imports
import config
import text
import data

def kbd_main():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in data.main_btns:
        keyboard.add(btn)
    return keyboard


bot = telebot.TeleBot(config.TOKEN, parse_mode="Markdown")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, text.about_bot, reply_markup=kbd_main())
    print(message)

bot.polling()

