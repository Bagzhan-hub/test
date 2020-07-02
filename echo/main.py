from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from subprocess import Popen
from subprocess import PIPE
from config import Tg_token
def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Привет! Отправь мне что-нибудь',
    )

def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Это учебный бот\nСписок доступных команд есть в меню\nТак же я отвечу на любой ваш вопрос',
    )

def do_time(bot: Bot, update: Update):
    process=Popen(["date"], stdout=PIPE)
    text, error = process.communicate()
    if error:
        text='Произошла ошибка, время неизвестно'
    else:
        text=text.decode("utf-8")
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )
def do_echo(bot: Bot, update: Updater):
    chat_id=update.message.chat_id
    text='Ваш ID= {}\n\n{}'.format(chat_id, update.message.text)
    bot.send_message(
        chat_id=chat_id,
        text=text,
    )
def new_changed(self):
    return 'hello'

def new_changed2(self):
    return 1+2
    
def main():
    bot=Bot(
        token=Tg_token,
        
    )
    updater= Updater(
        bot=bot,
    )
    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help)
    time_handler = CommandHandler('time', do_time)
    message_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)

    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()