import telebot
from password import gen,cube

    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("token")
    
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Команды: /hello, /bye, /password, /cube!")
    
@bot.message_handler(commands=['hello', 'hi', 'hey'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['cube'])
def send_cube(message):
    bot.reply_to(message, f'Вам выпало: {cube(6)}')

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
@bot.message_handler(commands=['password'])
def send_password(message):
    command_count=message.text.split()
    if len(command_count)>1:
        if 8<=int(command_count[1])<=20:
            bot.reply_to(message, f'Ваш пароль: {gen(int(command_count[1]))}')
        else:
            bot.reply_to(message, 'Введите длину пароля от 8 до 20')
    else:
        bot.reply_to(message, 'Вы не указали длину пароля')
        

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()
