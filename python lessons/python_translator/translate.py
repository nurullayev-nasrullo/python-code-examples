from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "6873235280:AAEvX9akGiH_2WFA5DJ9aZAXXC4HWoKWJJ0"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalomu alaykum, Xush kelibsiz!"
    answer += "\nMatn kiriting:"
    bot.reply_to(message, answer)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))

bot.infinity_polling()