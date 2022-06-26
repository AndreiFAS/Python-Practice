from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler


def hi(update, context):
    context.bot.send_message(update.effective_chat.id,
                             f'Привет {update.effective_user.first_name}!')


def info(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Тренировочный бот для практики на Python")


def sum(update, context):
    msg = update.message.text
    print(msg)
    lst = msg.split()
    if len(lst) == 3:
        a = float(lst[1])
        b = float(lst[2])
        context.bot.send_message(update.effective_chat.id, f'{a} + {b} = {a+b}')
    elif len(lst) == 5:
        a = complex(float(lst[1]), float(lst[2]))
        b = complex(float(lst[3]), float(lst[4]))
        context.bot.send_message(update.effective_chat.id, f'{a} + {b} = {a+b}')
    else:
        context.bot.send_message(update.effective_chat.id,'Ошибка ввода!')


def dif(update, context):
    msg = update.message.text
    print(msg)
    lst = msg.split()
    if len(lst) == 3:
        a = float(lst[1])
        b = float(lst[2])
        context.bot.send_message(update.effective_chat.id, f'{a} - {b} = {a-b}')
    elif len(lst) == 5:
        a = complex(float(lst[1]), float(lst[2]))
        b = complex(float(lst[3]), float(lst[4]))
        context.bot.send_message(update.effective_chat.id, f'{a} - {b} = {a-b}')
    else:
        context.bot.send_message(update.effective_chat.id,'Ошибка ввода!')


def mult(update, context):
    msg = update.message.text
    print(msg)
    lst = msg.split()
    if len(lst) == 3:
        a = float(lst[1])
        b = float(lst[2])
        context.bot.send_message(update.effective_chat.id, f'{a} * {b} = {a*b}')
    elif len(lst) == 5:
        a = complex(float(lst[1]), float(lst[2]))
        b = complex(float(lst[3]), float(lst[4]))
        context.bot.send_message(update.effective_chat.id, f'{a} * {b} = {a*b}')
    else:
        context.bot.send_message(update.effective_chat.id,'Ошибка ввода!')


def div(update, context):
    msg = update.message.text
    print(msg)
    lst = msg.split()
    if len(lst) == 3:    
        a = float(lst[1])
        b = float(lst[2])
        context.bot.send_message(update.effective_chat.id, f'{a} / {b} = {a/b}')
    elif len(lst) == 5:
        a = complex(float(lst[1]), float(lst[2]))
        b = complex(float(lst[3]), float(lst[4]))
        context.bot.send_message(update.effective_chat.id, f'{a} / {b} = {a/b}')
    else:
        context.bot.send_message(update.effective_chat.id,'Ошибка ввода!')


def add(update, context):
    msg = update.message.text
    print(msg)
    lst = msg.split()
    context.bot.send_message(update.effective_chat.id, f'Добавил {lst[1]} {lst[2]} {lst[3]} в справочник!')
    with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork009\BD.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{lst[1]};{lst[2]};{lst[3]}\n')


def read(update, context):
    with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork009\BD.csv', 'r', encoding='utf-8') as file:
        lst = (''.join(file)).split('\n')
        for i in lst:
            context.bot.send_message(update.effective_chat.id, f'{" ".join(list(i.split(";")))}')


def find(update, context):
    msg = update.message.text
    lst = msg.split()
    with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork009\BD.csv', 'r', encoding='utf-8') as file:
        lst_b = (''.join(file)).split('\n')
        for i in lst_b:
            if i.find(lst[1]) >= 0:
                context.bot.send_message(update.effective_chat.id, f'{" ".join(list(i.split(";")))}')