# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.


from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import bot_command as bc

with open('/Old/HomeWork009/_token.txt', 'r', encoding='utf-8') as file:
    token = file.readline()

bot = Bot(token)
updater = Updater(token, use_context=True)


updater.dispatcher.add_handler(CommandHandler('hello', bc.hi))
updater.dispatcher.add_handler(CommandHandler('info', bc.info))

# Калькулятор (требуется коррекный ввод данных через пробел!)
# комманда число число - для рациональных
# комманда вещ_часть мнимая_часть вещ_часть мнимая_часть - для комплексных
updater.dispatcher.add_handler(CommandHandler('sum', bc.sum))
updater.dispatcher.add_handler(CommandHandler('dif', bc.dif))
updater.dispatcher.add_handler(CommandHandler('mult', bc.mult))
updater.dispatcher.add_handler(CommandHandler('div', bc.div))

# Телефонный справочник (требуется коррекный ввод данных через пробел!)
# /add Имя телефон комментарий
# /find Имя_разыскиваемого
updater.dispatcher.add_handler(CommandHandler('add', bc.add))
updater.dispatcher.add_handler(CommandHandler('read', bc.read))
updater.dispatcher.add_handler(CommandHandler('find', bc.find))


print('Бот запущен!')
updater.start_polling()
updater.idle()
