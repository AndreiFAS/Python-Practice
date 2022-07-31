from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from bot_log import *


def hi(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id,
                             f'Привет {update.effective_user.first_name}!')


def info(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id,
                             "Тренировочный бот для практики на Python")


def sum(update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    lst = msg.split()
    if len(lst) == 3:
        a = float(lst[1])
        b = float(lst[2])
        context.bot.send_message(
            update.effective_chat.id, f'{a} + {b} = {a+b}')
    elif len(lst) == 5:
        a = complex(float(lst[1]), float(lst[2]))
        b = complex(float(lst[3]), float(lst[4]))
        context.bot.send_message(
            update.effective_chat.id, f'{a} + {b} = {a+b}')
    else:
        context.bot.send_message(update.effective_chat.id, 'Ошибка ввода!')


def dif(update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    lst = msg.split()
    if len(lst) == 3:
        a = float(lst[1])
        b = float(lst[2])
        context.bot.send_message(
            update.effective_chat.id, f'{a} - {b} = {a-b}')
    elif len(lst) == 5:
        a = complex(float(lst[1]), float(lst[2]))
        b = complex(float(lst[3]), float(lst[4]))
        context.bot.send_message(
            update.effective_chat.id, f'{a} - {b} = {a-b}')
    else:
        context.bot.send_message(update.effective_chat.id, 'Ошибка ввода!')


def mult(update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    lst = msg.split()
    if len(lst) == 3:
        a = float(lst[1])
        b = float(lst[2])
        context.bot.send_message(
            update.effective_chat.id, f'{a} * {b} = {a*b}')
    elif len(lst) == 5:
        a = complex(float(lst[1]), float(lst[2]))
        b = complex(float(lst[3]), float(lst[4]))
        context.bot.send_message(
            update.effective_chat.id, f'{a} * {b} = {a*b}')
    else:
        context.bot.send_message(update.effective_chat.id, 'Ошибка ввода!')


def div(update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    lst = msg.split()
    if len(lst) == 3:
        a = float(lst[1])
        b = float(lst[2])
        context.bot.send_message(
            update.effective_chat.id, f'{a} / {b} = {a/b}')
    elif len(lst) == 5:
        a = complex(float(lst[1]), float(lst[2]))
        b = complex(float(lst[3]), float(lst[4]))
        context.bot.send_message(
            update.effective_chat.id, f'{a} / {b} = {a/b}')
    else:
        context.bot.send_message(update.effective_chat.id, 'Ошибка ввода!')


def step(update, context):
    log(update, context)
    global candys
    msg = update.message.text
    print(msg)
    lst = msg.split()
    player_step = int(lst[1])
    if player_step > 9:
        player_step = 9
    elif player_step < 1:
        player_step = 1
    candys -= player_step
    context.bot.send_message(
        update.effective_chat.id, f'Вы взяли {player_step} конфет. Осталось {candys} конфет')
    if candys <= 10:
        context.bot.send_message(
            update.effective_chat.id, 'Вы победили! Чтобы начать новую игру наберите команду game.')
    else:
        bot_step = candys % 10  # Умный бот
        if bot_step > 9:
            bot_step = 9
        elif bot_step < 1:
            bot_step = 1
        candys -= bot_step
        context.bot.send_message(
            update.effective_chat.id, f'Я беру {bot_step} конфет. Осталось {candys} конфет')
        if candys <= 10:
            context.bot.send_message(
                update.effective_chat.id, 'Бот победил! Чтобы начать новую игру наберите команду game.')


def game(update, context):
    log(update, context)
    global candys
    candys = 100
    context.bot.send_message(
        update.effective_chat.id, f'Начинаем игру с конфетами.\nВсего {candys} конфет.\nМаксимум за ход можно взять 1 - 9 конфет.\nПобедит тот кто последним заберет последнии конфеты.\nЧтобы сделать ход введите команду step и число через пробел.')
