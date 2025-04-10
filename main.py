import telebot
from telebot import types

bot = telebot.TeleBot('7339440722:AAEoUj-exHRKwF9Fo0xtB9c5J1JjtfLBINs')

# Умовна база замовлень
orders = {
    "00012345": {"status": "Замовлення в обробці", "item": "Авокадо", "price": "1200 грн"},
    "00065432": {"status": "Замовлення очікує на пункті видачі", "item": "Батончик Energy", "price": "850 грн"},
    "00011122": {"status": "Замовлення виконане", "item": "Батончик Lite Energy", "price": "150 грн"},
}

# Функція для встановлення команд залежно від мови
def set_bot_commands(language):
    bot.delete_my_commands()  # Видаляємо попередні команди
    if language == "🇺🇦 Українська":
        commands = [telebot.types.BotCommand("/start", "Почати роботу")]
    else:  # Англійська
        commands = [telebot.types.BotCommand("/start", "Start working")]
    bot.set_my_commands(commands)

# Основне меню
def main_menu(message, lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if lang == "🇺🇦 Українська":
        btn1 = types.KeyboardButton("📦 Інформація про товари")
        btn2 = types.KeyboardButton("🔍 Перевірити стан замовлення")
        btn3 = types.KeyboardButton("📞 Контактна інформація")
        btn4 = types.KeyboardButton("❓ Часті запитання (FAQ)")
        btn5 = types.KeyboardButton("👩‍💼 Cпілкування з оператором")
        text = "Виберіть опцію:"
    else:  # Англійська
        btn1 = types.KeyboardButton("📦 Product Information")
        btn2 = types.KeyboardButton("🔍 Check Order Status")
        btn3 = types.KeyboardButton("📞 Contact Information")
        btn4 = types.KeyboardButton("❓ Frequently Asked Questions (FAQ)")
        btn5 = types.KeyboardButton("👨‍💼 Talk to Operator")
        text = "Choose an option:"
    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5)
    bot.send_message(message.chat.id, text, reply_markup=markup)

# Обробка команди /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇺🇦 Українська")
    btn2 = types.KeyboardButton("🇬🇧 English")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Вітання! 👋")
    bot.send_message(message.chat.id, "🇺🇦 Оберіть мову / 🇬🇧 Choose your language", reply_markup=markup)

# Обробка вибору мови
@bot.message_handler(func=lambda message: message.text in ["🇺🇦 Українська", "🇬🇧 English"])
def choose_language(message):
    lang = message.text
    set_bot_commands(lang)  # Встановлюємо команди залежно від обраної мови
    main_menu(message, lang)

# Меню і відповіді
@bot.message_handler(func=lambda message: message.text in [
    "📦 Інформація про товари", "🔍 Перевірити стан замовлення", "📞 Контактна інформація",
    "❓ Часті запитання (FAQ)", "👩‍💼 Cпілкування з оператором",
    "📦 Product Information", "🔍 Check Order Status", "📞 Contact Information",
    "❓ Frequently Asked Questions (FAQ)", "👨‍💼 Talk to Operator"
])
def menu(message):
    text = message.text
    if text in ["📦 Інформація про товари", "📦 Product Information"]:
        bot.send_message(
            message.chat.id,
            "📦 Інформація про товари:\n1. Навушники - 1200 грн\n2. Повербанк - 850 грн\n3. USB кабель - 150 грн"
            if text == "📦 Інформація про товари" else
            "📦 Product Information:\n1. Headphones - $30\n2. Power Bank - $22\n3. USB Cable - $5"
        )
    elif text in ["🔍 Перевірити стан замовлення", "🔍 Check Order Status"]:
        bot.send_message(
            message.chat.id,
            "🔍 Введіть номер замовлення у форматі: /00012345"
            if text == "🔍 Перевірити стан замовлення" else
            "🔍 Please enter your order number in format: /00012345"
        )
    elif text in ["📞 Контактна інформація", "📞 Contact Information"]:
        bot.send_message(
            message.chat.id,
            "📞 Телефон: +380123456789\n📧 Email: info@example.com"
            if text == "📞 Контактна інформація" else
            "📞 Phone: +123456789\n📧 Email: info@example.com"
        )
    elif text in ["❓ Часті запитання (FAQ)", "❓ Frequently Asked Questions (FAQ)"]:
        bot.send_message(
            message.chat.id,
            "❓ FAQ:\n- Як замовити товар?\n- Як оплатити?\n- Які умови доставки?"
            if text == "❓ Часті запитання (FAQ)" else
            "❓ FAQ:\n- How to place an order?\n- How to pay?\n- Delivery terms?"
        )
    elif text in ["👩‍💼 Cпілкування з оператором", "👨‍💼 Talk to Operator"]:
        bot.send_message(
            message.chat.id,
            "👩‍💼 Очікуйте на з'єднання з оператором..."
            if text == "👩‍💼 Cпілкування з оператором" else
            "👨‍💼 Please wait, connecting to operator..."
        )

# Обробка статусу замовлення
@bot.message_handler(func=lambda message: message.text.startswith('/'))
def check_order_status(message):
    order_id = message.text[1:]
    order = orders.get(order_id)
    if order:
        response = f"📦 Статус: {order['status']}\n🛒 Товар: {order['item']}\n💵 Ціна: {order['price']}"
    else:
        response = "❌ Замовлення не знайдено. Перевірте номер та спробуйте ще раз."
    bot.send_message(message.chat.id, response)

# Запуск бота
if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {e}")
