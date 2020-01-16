import signal, os
import logging
from time import sleep
from telegram import ChatAction
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

TOKEN = os.environ.get('TOKEN', '')
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logging.info('Starting up!')

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def restart(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    sleep(1)
    bot.sendMessage(update.message.chat_id, "Bot is restarting...")
    sleep(1)
    os.kill(os.getpid(), signal.SIGTERM)

def photo(bot, update):
    bot.sendPhoto(update.message.chat_id, photo='https://telegram.org/img/t_logo.png')

def boobs(bot, update):
    bot.sendPhoto(update.message.chat_id, photo='https://pbs.twimg.com/media/Cut_RiXWYAArLZX.jpg')

def butt(bot, update):
    bot.sendPhoto(update.message.chat_id, photo='https://i.ytimg.com/vi/m7DVnuIq_4c/hqdefault.jpg')

dispatcher.add_handler(MessageHandler(Filters.text, echo))
dispatcher.add_handler(CommandHandler('caps', caps, pass_args=True))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('restart', restart))
dispatcher.add_handler(CommandHandler('photo', photo))
dispatcher.add_handler(CommandHandler('boobs', boobs))
dispatcher.add_handler(CommandHandler('butt', butt))

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.setWebhook("https://tranquil-lake-76341.herokuapp.com/" + TOKEN)
updater.idle()

logging.info('Exiting!')

