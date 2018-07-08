import logging
import os

from models import tuling

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    update.effective_message.reply_text("Hi!")


def echo(bot, update):
    update.effective_message.reply_text(update.effective_message.text)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def tl(bot, update):
    data = {
        'info': update.effective_message.text,
    }
    r = tuling.Tuling().text(**data)
    update.effective_message.reply_text(r)


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    NAME = os.environ.get('APP_NAME')

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.debug([TOKEN, NAME, PORT])

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('tuling', tl))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
