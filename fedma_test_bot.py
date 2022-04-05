import telebot
import bot_id

bot = telebot.TeleBot(bot_id.id)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("user wrote: ", message)
    bot.reply_to(message, "Давайте решим задачу # 19 ! Введите любое число")
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Спасибо за"+ message.text)
    print(message.text)
    filePath = 'D:\\Razrabitchik\\python\\telegram_bot\\numbers.txt'
    file = open(filePath, 'a')
    numbers = ""
    
    for c in message.text:
        if ord(c) <= ord('9') and ord(c) >= ord('0'):
            numbers += c
    file.write(numbers + "\n")
    file.close()
    

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     print("user wrote: ", message)
#     bot.reply_to(message, "Thets resolve # 19 together! Enter the number")
#     filePath = 'numbers.txt'
#     file = open(filePath, 'a')
#     file.write(message)

# func1 = lambda x, y: x+y
# def func2(x,y):
#     return x+y
# print(func1(1,2))
# print(func2(1,2))

# @bot.message_handler(commands=['name'])
# def send_name(message):
#     print("user wrote: ", message)
#     bot.reply_to(message, "Your name is " + str(message.from_user.first_name) + " " + str(message.from_user.last_name))

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     print("user wrote: ", message)
#     bot.reply_to(message, "Text of your message is:\n" + message.text)

bot.infinity_polling()
