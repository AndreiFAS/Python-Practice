from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler


def log(update, context):
    with open('/Old/HomeWork010/logs.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{update.effective_user.id};{update.effective_user.first_name};{update.message.text}\n')