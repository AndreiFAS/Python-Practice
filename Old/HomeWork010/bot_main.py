# Прикрутить бота к задачам с предыдущего семинара:
# 1. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
# 2.1 Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 2.2 Задачи с конфетами
# 2.1 или 2.2 - на выбор

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import bot_com as bc

with open('/Old/HomeWork009/_token.txt', 'r', encoding='utf-8') as file:
    token = file.readline()

bot = Bot(token)
updater = Updater(token, use_context=True)


updater.dispatcher.add_handler(CommandHandler('hello', bc.hi))
updater.dispatcher.add_handler(CommandHandler('info', bc.info))

# Калькулятор (требуется коррекный ввод данных через пробел! добавил логирование)
# комманда число число - для рациональных
# комманда вещ_часть мнимая_часть вещ_часть мнимая_часть - для комплексных
updater.dispatcher.add_handler(CommandHandler('sum', bc.sum))
updater.dispatcher.add_handler(CommandHandler('dif', bc.dif))
updater.dispatcher.add_handler(CommandHandler('mult', bc.mult))
updater.dispatcher.add_handler(CommandHandler('div', bc.div))

# Игра с конфетами
updater.dispatcher.add_handler(CommandHandler('game', bc.game))
updater.dispatcher.add_handler(CommandHandler('step', bc.step))

print('Бот запущен!')
updater.start_polling()
updater.idle()
