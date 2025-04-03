import telebot
from telebot import types

bot = telebot.TeleBot('7339440722:AAEoUj-exHRKwF9Fo0xtB9c5J1JjtfLBINs')

@bot.message_handler(commands = ['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇺🇦 Українська")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup1.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Вітання")
    bot.send_message(message.from_user.id, "🇺🇦 Оберіть мову / 🇬🇧 Choose your language", reply_markup=markup1)

@bot.message_handler(func=lambda message: message.text in ['🇺🇦 Українська', '🇬🇧 English'])
def choose_language(message):
    if message.text == '🇺🇦 Українська':
        # Меню українською
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Інформація про товари")
        btn2 = types.KeyboardButton("Перевірити стан замовлення")
        btn3 = types.KeyboardButton("Контактна інформація")
        btn4 = types.KeyboardButton("Часті запитання (FAQ)")
        btn5 = types.KeyboardButton("Cпілкування з оператором")
        markup.add(btn1, btn2, btn3)
        markup.add(btn4, btn5)
        bot.send_message(message.from_user.id, "Меню українською мовою:", reply_markup=markup)
    
    elif message.text == '🇬🇧 English':
        # Меню англійською
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Product information")
        btn2 = types.KeyboardButton("Check the status of your order")
        btn3 = types.KeyboardButton("Contact information")
        btn4 = types.KeyboardButton("Frequently asked questions")
        btn5 = types.KeyboardButton("Communication with the operator")
        markup.add(btn1, btn2, btn3)
        markup.add(btn4, btn5)
        bot.send_message(message.from_user.id, "Menu in English:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in [
    "Інформація про товари", "Перевірити стан замовлення", "Контактна інформація", "Часті запитання (FAQ)", "Cпілкування з оператором",
    "Product information", "Check the status of your order", "Contact information", "Frequently asked questions", "Communication with the operator"
])
def menu(message):
    if message.text == "Інформація про товари":

    elif message.text == "Перевірити стан замовлення":
    
    elif message.text == "Контактна інформація":
    
    elif message.text == "Часті запитання (FAQ)":

    elif message.text == "Cпілкування з оператором":

    elif message.text == "Product information":

    elif message.text == "Check the status of your order":
    
    elif message.text == "Contact information":
    
    elif message.text == "Frequently asked questions":
    
    elif message.text == "Communication with the operator":

        https://magistratura.in.ua/quizzes/efvv-it-rozdil-1-algorytmy-ta-obchyslyuvalna-skladnist-1-1-osnovy-struktury-danyh-i-algorytmy/
bot.polling(none_stop=True, interval=0)